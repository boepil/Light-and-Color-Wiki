import path from "path"
import { readFileSync, readdirSync, statSync, existsSync } from "fs"

const publicDir = path.resolve(process.argv[2] ?? "public")

function walk(dir) {
  const out = []
  for (const entry of readdirSync(dir)) {
    const full = path.join(dir, entry)
    if (statSync(full).isDirectory()) out.push(...walk(full))
    else if (entry.endsWith(".html")) out.push(full)
  }
  return out
}

function resolveTarget(base, href) {
  if (href.startsWith("#")) return null // in-page anchor
  if (/^(https?:|mailto:|data:)/.test(href)) return null // external
  const withoutHash = href.split("#")[0]
  if (!withoutHash) return null
  const target = path.resolve(path.dirname(base), withoutHash)
  if (existsSync(target)) return null // exact file hit
  if (existsSync(target + ".html")) return null // Quartz extensionless slug
  if (existsSync(path.join(target, "index.html"))) return null // folder index
  return target
}

const files = walk(publicDir)
const broken = []
const external = []

for (const file of files) {
  const content = readFileSync(file, "utf-8")
  const hrefs = [...content.matchAll(/href="([^"]+)"/g)].map((m) => m[1])
  for (const href of hrefs) {
    if (href.startsWith("http")) {
      external.push(href)
      continue
    }
    const missing = resolveTarget(file, href)
    if (missing) broken.push({ page: path.relative(publicDir, file), href, missing })
  }
}

console.log(`Checked ${files.length} pages`)
console.log(`External links: ${external.length} (not validated)`)
console.log(`Broken internal links: ${broken.length}`)
for (const b of broken) {
  console.log(`  BROKEN: ${b.page} -> "${b.href}" (missing ${path.relative(publicDir, b.missing)})`)
}
