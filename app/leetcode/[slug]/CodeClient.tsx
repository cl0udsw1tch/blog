'use client'
import { useEffect } from 'react';
import Prism from "@/data/leetcode/solutions"
import 'prismjs/themes/prism-dark.css'

import { LeetCodeData } from '@/data/leetcode/solutions';


import Markdown from 'react-markdown';


const ext2lang: { [key: string]: string } = {
	'py': 'python'
}
export default function CodeClient({ problem, codeBlock, codeDesc }: { problem: LeetCodeData, codeBlock: string, codeDesc: string }) {
	useEffect(() => {
		// This executes exactly once when the component mounts on the screen
		Prism.highlightAll();
	}, []);

	return (
		<div className="problem page-content">
			<aside >
				<div className="meta">
					<h1>{problem.title}</h1>

					<div className="problem page-details">
						<span>{problem.category}</span> · <span>{problem.date}</span>
					</div>

					<div dangerouslySetInnerHTML={{ __html: codeDesc }} />

				</div>
			</aside>
			<article>
				<h1 className="text-4xl">Problem: {problem.title}</h1>
				<pre>
					<code className={"font-mono w-0.5" + " language-" + ext2lang[problem.type]}>
						{codeBlock}
					</code>

				</pre>

			</article>
		</div>

	);
}

