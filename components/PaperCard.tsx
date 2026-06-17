import Link from "next/link";
import { PaperMeta } from "@/papers/papers";

export default function PaperCard({ paper }: { paper: PaperMeta }) {
    return (
        <Link href={`/${paper.slug}`} className="paper-card">
            <div className="paper-meta">
                <span className="paper-category">{paper.category}</span>
                <span className="paper-date">{paper.date}</span>
            </div>

            <h3>{paper.title}</h3>
            <p>{paper.description}</p>
        </Link>
    );
}
