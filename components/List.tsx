import MetaData from "./MetaData";
import Card from "./Card";


export default function List<T extends MetaData>({
    items,
}: {
    items: T[];
}) {
    const grouped = items.reduce((acc, paper) => {
        if (!acc[paper.category]) {
            acc[paper.category] = [];
        }
        acc[paper.category].push(paper);
        return acc;
    }, {} as Record<string, T[]>);

    return (
        <div className="list container">
            {Object.entries(grouped).map(([category, items]) => (
                <section key={category} className="list-category-group">
                    <h3 className="list-category-title">{category}</h3>

                    <div className="list-category-list">
                        {items.map((item) => (
                            <Card key={item.slug} metaData={item} />
                        ))}
                    </div>
                </section>
            ))}
        </div>
    );
}
