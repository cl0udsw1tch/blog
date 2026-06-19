'use client'

import PaperList from "@/components/PaperList";
import { papers } from "@/papers/papers";
import Link from "next/link";
import { useState } from "react";

export default function Home() {
    const [visible, setVisible] = useState('landing')
    return (
        <main className="container">
            {/* HERO SECTION */}
            <section className="hero">
                <h1>The Contraction</h1>
                <p>
                    A collection of articles on Math, AI, Engineering and Computer Science.
                    Built as a personal research archive.
                </p>

                <div className="hero-actions">
                    <Link href="#papers" className="button" onClick={() => {
                        if (visible !== 'landing') {
                            setVisible('landing');

                        }
                    }}>
                        View Papers
                    </Link>

                    <Link href="#about" className="button secondary">
                        Leetcode
                    </Link>
                </div>
            </section>

            <section className="landing">
                {/* INTRO / CONTEXT */}
                <section className="intro">
                    <h2>About this site</h2>
                    <p>
                        This site contains  notes and technical papers written
                        while exploring machine learning systems, mathematics in general and related technical topics.
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


            </section>

            <section className="leetcode">

            </section>
        </main>
    );
}
