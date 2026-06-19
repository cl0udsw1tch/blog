'use client'
import { useMemo } from "react";


export type TocNode = {
    id: string,
    title: string,
    depth: number,
    children: TocNode[],
};


function parseSection(
    section: HTMLElement,
    depth = 0
): TocNode | null {
    const children = Array.from(section.children)
        .filter(
            (child) =>
                child instanceof HTMLElement &&
                child.tagName === "SECTION"
        )
        .map((child) =>
            parseSection(child as HTMLElement, depth + 1)
        )
        .filter(Boolean) as TocNode[];

    return {
        id: section.id,
        title:
            section.dataset.title ??
            section.id,
        depth,
        children,
    };
}

export function buildToc(container: HTMLElement): TocNode[] {
    const topLevelSections = Array.from(container.children).filter(
        (el): el is HTMLElement =>
            el instanceof HTMLElement &&
            el.tagName === "SECTION"
    );

    return topLevelSections
        .map((section) => parseSection(section, 0))
        .filter(Boolean) as TocNode[];
}

export function flattenToc(nodes: TocNode[]): TocNode[] {
    const result: TocNode[] = [];

    function walk(nodeList: TocNode[]) {
        for (const node of nodeList) {
            result.push(node);
            if (node.children?.length) {
                walk(node.children);
            }
        }
    }

    walk(nodes);
    return result;
}
type Props = {
    toc: TocNode[];
    activeId?: string;
};

export function TocTree({ toc, activeId }: Props) {
    const items = useMemo(() => toc, [toc]);

    return (
        <nav className="toc">
            {items.map((item) => {
                const isActive = item.id === activeId;

                return (
                    <div
                        key={item.id}

                    >
                        <a
                            href={`#${item.id}`}
                            onClick={(e) => {
                                e.preventDefault();
                                document
                                    .getElementById(item.id)
                                    ?.scrollIntoView({
                                        behavior: "smooth",
                                        block: "start",

                                    });

                            }}
                            style={{
                                textDecorationLine: isActive ? "underline" : "none",
                                color: isActive ? "#000" : "#555",
                                width: '100%',
                                fontSize: item.depth <= 1 ? '1rem' : '0.8rem',
                                marginLeft: item.depth * 10,
                                maxWidth: '30vw'

                            }}
                        >
                            {item.title}
                        </a>
                    </div>
                );
            })}
        </nav>
    );
}
