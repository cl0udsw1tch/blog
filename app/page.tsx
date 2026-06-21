'use client'

import List from "@/components/List";
import { papers } from "@/papers/papers";
import { solutions } from "@/data/leetcode/solutions";
import { useState } from "react";



export default function Home() {
    const [visible, setVisible] = useState('landing')
    return (
        <main className="container" >
            {/* HERO SECTION */}
            <section className="hero">
                <h1>The Contraction</h1>
                <p>
                    A collection of articles on Math, AI, Engineering and Computer Science.
                    Built as a personal research archive.
                </p>

                <div className="hero-actions">
                    <button className={"button" + (visible === 'landing' ? '' : ' secondary')} onClick={() => {
                        if (visible !== 'landing') {
                            setVisible('landing');

                        }
                    }}>
                        View Papers
                    </button>

                    <button className={"button" + (visible === 'leetcode' ? '' : ' secondary')} onClick={() => {
                        setVisible('leetcode')
                    }}>
                        Leetcode
                    </button>
                </div>
            </section>

            <section className='landing' style={{ display: visible === 'landing' ? '' : 'none' }}>
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

                    <List items={papers} />
                </section>


            </section>

            <section className="leetcode" style={{ display: visible === 'leetcode' ? '' : 'none' }}>
                <div className="section-header">
                    <h2>All Solutions</h2>
                    <p>{solutions.length} published</p>
                </div>

                <List items={solutions} dropDown={true} />

            </section>
        </main >
    );
}
