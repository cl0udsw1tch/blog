import { PaperMeta } from "@/papers/papers";
import PaperCard from "./PaperCard";

export default function PaperList({
    papers,
}: {
    papers: PaperMeta[];
}) {
    const grouped = papers.reduce((acc, paper) => {
        if (!acc[paper.category]) {
            acc[paper.category] = [];
        }
        acc[paper.category].push(paper);
        return acc;
    }, {} as Record<string, PaperMeta[]>);

    return (
        <div className="paper-list container">
            {Object.entries(grouped).map(([category, items]) => (
                <section key={category} className="paper-category-group">
                    <h3 className="category-title">{category}</h3>

                    <div className="category-list">
                        {items.map((paper) => (
                            <PaperCard key={paper.slug} paper={paper} />
                        ))}
                    </div>
                </section>
            ))}
        </div>
    );
}
