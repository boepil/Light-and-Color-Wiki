import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "Light & Color Wiki",
    pageTitleSuffix: " · Light & Color Wiki",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "en-US",
    baseUrl: "boepil.github.io/Light-and-Color-Wiki",
    ignorePatterns: [
      "private",
      "templates",
      ".obsidian",
      "scripts",
      "website",
      ".git",
      ".agents",
      "raw_sources/notebooklm_*.md",
      "page-status.md",
      "AGENTS.md",
      "log.md",
      "llm-wiki.md",
      "to do.md",
      "README.md",
    ],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Source Serif 4",
        body: "Source Sans Pro",
        code: "IBM Plex Mono",
      },
      colors: {
        lightMode: {
          light: "#faf8f5",
          lightgray: "#e8e4dd",
          gray: "#b3a99b",
          darkgray: "#4a453e",
          dark: "#26221d",
          secondary: "#b0382c",
          tertiary: "#2f6f6f",
          highlight: "rgba(176, 56, 44, 0.10)",
          textHighlight: "#ffd54a66",
        },
        darkMode: {
          light: "#16151a",
          lightgray: "#33313a",
          gray: "#5c5866",
          darkgray: "#d6d3dc",
          dark: "#eceaf0",
          secondary: "#d97a6d",
          tertiary: "#6faeae",
          highlight: "rgba(217, 122, 109, 0.15)",
          textHighlight: "#b3aa0288",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.CleanPages(),
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      Plugin.CustomOgImages(),
    ],
  },
}

export default config
