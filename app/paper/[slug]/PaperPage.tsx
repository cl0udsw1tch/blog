import { notFound } from "next/navigation";
import { papers } from "@/papers/papers";
import fs from "fs";
import path from "path";
import PageClient from "./PageClient";

export default async function PaperPage({ page }: { page: string }) {

    const paper = papers.find((p) => p.slug === page);

    if (!paper) {
        notFound();
    }

    if (paper.type === "pdf") {

        return (
            <main style={{ height: '100%' }}>
                <h1>{paper.title}</h1>

                <div className="paper page-meta">
                    <span>{paper.category}</span> · <span>{paper.date}</span>
                </div>
                <iframe
                    src={`/papers/${paper.file}`}
                    className="pdf-viewer"
                    style={{ width: '80vw', height: '80%' }}
                />

            </main>
        );
    }


    const filePath = path.join(
        process.cwd(),
        "papers",
        paper.file
    );

    const html = fs.readFileSync(filePath, "utf8");


    return (

        <PageClient html={html} paper={paper} />

    );
}
