import { QuartzTransformerPlugin } from "../types"
import { Root, Heading } from "mdast"
import { visit } from "unist-util-visit"

const REMOVE_SECTIONS = new Set(["Subtopics", "Cross-References"])

export const CleanPages: QuartzTransformerPlugin = () => {
  return {
    name: "CleanPages",
    markdownPlugins() {
      return [
        () => {
          return (tree: Root, _file) => {
            const toRemove: number[] = []

            visit(tree, "heading", (node: Heading, index: number | undefined, parent) => {
              if (!parent || index === undefined) return
              const text = ((node.children ?? []) as Array<{ value?: string }>)
                .map((c) => c.value ?? "")
                .join("")
                .trim()

              if (node.depth === 2 && REMOVE_SECTIONS.has(text)) {
                toRemove.push(index)
              }
            })

            const content = tree.children
            const removeIndices = new Set<number>()
            for (const idx of toRemove) {
              removeIndices.add(idx)
              // walk forward to remove the heading's following siblings
              // until the next heading of equal or greater depth
              let j = idx + 1
              while (j < content.length) {
                const sibling = content[j]
                const isHeading = sibling.type === "heading"
                if (isHeading) break
                removeIndices.add(j)
                j++
              }
            }

            tree.children = content.filter((_, i) => !removeIndices.has(i))
          }
        },
      ]
    },
  }
}
