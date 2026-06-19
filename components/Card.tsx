import Link from "next/link";
import MetaData from "@/components/MetaData";

export default function Card<T extends MetaData>({ metaData }: { metaData: T }) {
    return (
        <Link href={`/${metaData.class}/${metaData.slug}`} className="list-item-card">
            <div className="list-item-meta">
                <span className="list-item-category">{metaData.category}</span>
                <span className="list-item-date">{metaData.date}</span>
            </div>

            <h3>{metaData.title}</h3>
            <p>{metaData.description}</p>
        </Link>
    );
}
