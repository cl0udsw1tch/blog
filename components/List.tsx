import MetaData from "./MetaData";
import Card from "./Card";
import { useState } from "react";
import { useMemo } from "react";

export function CategoryTabs({ active }: { active: Record<string, boolean> }) {


    return (
        <div className="category-tabs">
            {Object.keys(active).map((key) =>

            (<button key={key} className={`category-tab-${active[key]}` + active[key] ? "" : "secondary"}  >
                {key}
            </button>))}
        </div >
    )
}


export default function List<T extends MetaData>({
    items, dropDown = false
}: {
    items: T[], dropDown?: boolean;
}) {


    const grouped = useMemo(() => items.reduce((acc, paper) => {
        if (!acc[paper.category]) {
            acc[paper.category] = [];
        }
        acc[paper.category].push(paper);
        return acc;
    }, {} as Record<string, T[]>), [items]

    )
    const [activeCategories, setActiveCategories] = useState(Object.fromEntries(Object.keys(grouped).map(k => [k, false])))


    return (
        <div className="list container">
            <div className="category-tabs">
                {Object.keys(activeCategories).map((k) =>

                (<button key={k} className={`category-tab-${k} ` + (activeCategories[k] ? "button" : "button secondary")} onClick={() => { setActiveCategories(prev => ({ ...prev, [k]: !prev[k] })) }}>
                    {k}
                </button>))}
            </div >
            {Object.entries(grouped).filter(([k, v]) => activeCategories[k]).map(([category, items]) => (
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
