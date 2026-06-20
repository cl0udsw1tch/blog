import rehypeDocument from 'rehype-document'
import rehypeKatex from 'rehype-katex'
import rehypeParse from 'rehype-parse'
import rehypeStringify from 'rehype-stringify'
import rehypeRaw from 'rehype-raw'
import rehypeMathjax from 'rehype-mathjax'
import rehypeEasytex from 'rehype-easytex'

import { read, write } from 'to-vfile'
import { unified } from 'unified'
import path from 'path'
import fs, { existsSync } from "node:fs"
import { exists } from "node:fs"

console.log(process.env)
const paper = process.env.npm_config_paper;

if (!paper) {
  console.log("TEX-PIPELINE: Not rendering paper.")
  process.exit(0)
}

console.log("TEX-PIPELINE: paper renderered=" + paper)

const input_dir = path.join(process.cwd(), "papers", paper)
const input_path = path.join(input_dir.toString(), "input.html")

const output_dir = path.join(process.cwd(), "public", paper)
const output_path = path.join(output_dir.toString(), "index.html")

if (!existsSync(output_dir)) {
  try {
    fs.mkdirSync(output_dir)
  } catch (e) {
    console.log("Error creating output folder: " + e.toString())
    process.exit(1)
  }
}

const file = await unified()
  .use(rehypeParse, { fragment: true })
  .use(rehypeEasytex)
  .use(rehypeKatex)
  // .use(rehypeDocument, {
  //     css: 'https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css'
  // })
  .use(rehypeStringify, { fragment: true })
  .process(await read(input_path))

file.path = output_path
await write(file)
