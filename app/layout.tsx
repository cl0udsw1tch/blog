import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import Link from "next/link";
import Home from "@/components/home";
import { Inter } from 'next/font/google'
import { Playfair_Display } from "next/font/google";
import { Open_Sans, Lato } from "next/font/google";
import "prismjs/themes/prism-tomorrow.css";


const geistSans = Geist({
    variable: "--font-geist-sans",
    subsets: ["latin"],
});

const geistMono = Geist_Mono({
    variable: "--font-geist-mono",
    subsets: ["latin"],
});

const opensans = Open_Sans({
    variable: "--font-open-sans",
    subsets: ["latin"],
});
const lato = Lato({
    variable: "--font-lato",
    subsets: ["latin"],
    weight: ['400']
});


export const metadata: Metadata = {
    title: "Math and AI blog by Nurein Umeya.",
    description: "Machine Learning, AI, Engineering, Computer Science...",
};


const inter = Inter({
    subsets: ['latin'],
    variable: '--font-inter', // This creates the variable
})
const playfair = Playfair_Display({
    subsets: ['latin'],
    weight: ['400', '700'],
    variable: '--font-playfair',
})

export default function RootLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>) {

    return (
        <html
            lang="en"
            className={`${lato.variable} ${opensans.variable} ${playfair.variable} ${inter.variable} ${geistSans.variable} ${geistMono.variable} h-full antialiased`}
        >
            <head>
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css" />
            </head>
            <body className="min-h-full min-w-full flex flex-col justify-start items-center">
                <header className="basis-1 grow-0 shrink-0 p-12 pb-0">
                    <Home />

                </header>

                {children}

                <footer className="bg-black text-white p-5 pl-10 font-mono" >
                    <a href={'https://nureinumeya.vercel.app'}>About me</a>
                    <span> | </span>
                    <Link href={'mailto:nurein.umeya@alumni.utoronto.ca'}>Contact</Link>
                </footer>
            </body>

        </html>
    );
}
