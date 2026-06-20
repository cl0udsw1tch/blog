import { solutions } from "@/data/leetcode/solutions"
import { notFound } from "next/navigation"
import { readdirSync, readFileSync } from "fs"
import path from "path"
import { cwd } from "process"

import { parseUrl } from "next/dist/shared/lib/router/utils/parse-url"
import CodeClient from "./CodeClient"





export default async function page({ params }: { params: Promise<{ slug: string }> }) {
    const { slug } = await params
    const problem = solutions.find(p => {
        return (p.class === 'leetcode' && p.slug === decodeURIComponent(slug))
    })

    if (!problem) {
        notFound();
    }

    const folder = path.join(cwd(), 'data', 'leetcode', 'submissions', problem.title)


    const codeDesc = readFileSync(path.join(folder, problem.file), 'utf8')
    const files = readdirSync(folder)
    const codeBlock = readFileSync(path.join(folder, files.filter(f => f.endsWith(problem.type))[0]), 'utf8')


    return (

        <main className="page leetcode">
            <div className="problem page-content">
                <aside >
                    <div className="meta">
                        <h1>{problem.title}</h1>

                        <div className="problem page-details">
                            <span>{problem.category}</span> · <span>{problem.date}</span>
                        </div>

                    </div>
                </aside>


                <CodeClient problem={problem} codeBlock={codeBlock} codeDesc={codeDesc} />

            </div>

        </main>
    )
}
