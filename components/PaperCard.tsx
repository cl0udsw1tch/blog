import Link from "next/link";

export default function PaperCard({ paper }) {
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
