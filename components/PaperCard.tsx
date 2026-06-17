import Link from "next/link";

export default function PaperCard({ paper }) {
    return (
        <Link href={`/${paper.slug}`} className="paper-card">
            <h3>{paper.title}</h3>
            <p>{paper.description}</p>
        </Link>
    );
}
