// app/papers/[slug]/PageClient.tsx
"use client";

import { useEffect, useRef, useState, useLayoutEffect } from "react";
import { buildToc, flattenToc, TocTree } from "@/components/Toc";
import type { TocNode } from "@/components/Toc";
import type { PaperMeta } from "@/papers/papers"




export default function PageClient({ html, paper }: { html: string, paper: PaperMeta }) {
    const contentRef = useRef<HTMLDivElement | null>(null);
    const [toc, setToc] = useState<TocNode[]>([]);
    const [activeId, setActiveId] = useState<string>("");
    const [sectionsY, setSectionsY] = useState<{ id: string, y: number }[]>([])


    function getActiveSection(): string {
        const threshold = 200;

        let active = sectionsY[0]?.id ?? "";

        for (const section of sectionsY) {

            if (section.y - threshold <= window.scrollY) {
                active = section.id;
            } else {
                break;
            }
        }

        return active;
    }

    useEffect(() => {
        if (!contentRef.current) return;

        const tocData = flattenToc(buildToc(contentRef.current));
        setToc(tocData);

        const calcSectionY = () => {
            const sections = Array.from(
                contentRef.current?.querySelectorAll(
                    "section[id]"
                ) ?? []
            ) as HTMLElement[];
            const ys = sections.map(s => ({ id: s.id, y: s.getBoundingClientRect().top + window.scrollY }))
            setSectionsY(ys)

        }



        window.addEventListener("resize", calcSectionY)
        const ro = new ResizeObserver(calcSectionY);
        ro.observe(contentRef.current);

        return () => {

            window.removeEventListener('resize', calcSectionY)
            ro.disconnect()
        }

    }, [html])

    useLayoutEffect(() => {
        if (!contentRef.current) return;



        const onScrollEnd = () => {

            setActiveId(getActiveSection());
        };

        window.addEventListener("scrollend", onScrollEnd);
        onScrollEnd();

        return () => {
            console.log('killing')
            window.removeEventListener("scrollend", onScrollEnd);
        };
    }, [getActiveSection]);


    console.log(activeId)
    return (
        <div className="paper page-content" >
            <aside >
                <div className="meta">
                    <h1>{paper.title}</h1>

                    <div className="page-details">
                        <span>{paper.category}</span> · <span>{paper.date}</span>
                    </div>

                </div>
                <TocTree toc={toc} activeId={activeId} />
            </aside>

            <article
                ref={contentRef}
                dangerouslySetInnerHTML={{ __html: html }}
            />
        </div>
    );
}
