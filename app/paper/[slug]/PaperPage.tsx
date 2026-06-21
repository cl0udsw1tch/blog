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
            <div className="paper pdf page-content"  >
                <div className="meta" >
                    <h1>{paper.title}</h1>

                    <div className="page-details">
                        <span>{paper.category}</span> · <span>{paper.date}</span>
                    </div>
                </div>
                <article>
                    <iframe
                        src={`/papers/${paper.file}`}
                        className="pdf-viewer"
                        style={{ width: '80vw', height: '80%' }}
                    />
                </article>
            </div>

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
