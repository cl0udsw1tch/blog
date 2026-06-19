import { solutions } from "@/data/leetcode/solutions"
import { notFound } from "next/navigation"
import { readFileSync } from "fs"
import path from "path"
import { cwd } from "process"
import { NextURL } from "next/dist/server/web/next-url"
import { parseUrl } from "next/dist/shared/lib/router/utils/parse-url"


export default async function page({ params }: { params: Promise<{ slug: string }> }) {
    const { slug } = await params
    const problem = solutions.find(p => {
        console.log(p.slug, decodeURIComponent(slug))
        return (p.class === 'leetcode' && p.slug === decodeURIComponent(slug))
    })

    if (!problem) {
        notFound();
    }

    const codeBlock = readFileSync(path.join(cwd(), 'data', 'leetcode', problem.file), 'utf8')


    return (

        <main className="leetcode">
            <h1 className="text-4xl">Problem: {problem.title}</h1>
            <code className="font-mono w-0.5">
                {codeBlock}
            </code>
        </main>
    )
}
