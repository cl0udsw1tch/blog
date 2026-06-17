import PaperList from "@/components/PaperList";
import { papers } from "@/papers/papers";
import Link from "next/link";

export default function Home() {
    return (
        <main className="container">
            {/* HERO SECTION */}
            <section className="hero">
                <h1>Research Notes</h1>
                <p>
                    A collection of papers on AI, systems, and computer science.
                    Built as a personal research archive.
                </p>

                <div className="hero-actions">
                    <Link href="#papers" className="button">
                        View Papers
                    </Link>

                    <Link href="/about" className="button secondary">
                        About
                    </Link>
                </div>
            </section>

            {/* INTRO / CONTEXT */}
            <section className="intro">
                <h2>About this site</h2>
                <p>
                    This site contains research notes and technical papers written
                    while exploring machine learning systems, distributed computing,
                    and related topics.
                </p>
            </section>

            {/* PAPERS */}
            <section id="papers">
                <div className="section-header">
                    <h2>All Papers</h2>
                    <p>{papers.length} published</p>
                </div>

                <PaperList papers={papers} />
            </section>
        </main>
    );
}
