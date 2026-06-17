import { notFound } from "next/navigation";
import { papers } from "@/papers/papers";
import fs from "fs";
import path from "path";

export default async function PaperPage({
    params,
}: {
    params: Promise<{ slug: string }>;
}) {
    const { slug } = await params;

    const paper = papers.find((p) => p.slug === slug);

    if (!paper) {
        notFound();
    }

    const filePath = path.join(
        process.cwd(),
        "papers",
        paper.file
    );

    const html = paper.type === "html" ? <article className="paper-content" dangerouslySetInnerHTML={{ __html: fs.readFileSync(filePath, "utf8") }} /> : <iframe src={filePath} />;


    return (
        <main className="container">
            <h1>{paper.title}</h1>

            <div className="paper-meta">
                <span>{paper.category}</span> · <span>{paper.date}</span>
            </div>

            {html}
        </main>
    );
}
