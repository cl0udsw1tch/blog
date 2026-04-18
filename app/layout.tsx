import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import Link from "next/link";
import Home from "./components/home";

const geistSans = Geist({
    variable: "--font-geist-sans",
    subsets: ["latin"],
});

const geistMono = Geist_Mono({
    variable: "--font-geist-mono",
    subsets: ["latin"],
});

export const metadata: Metadata = {
    title: "Math and AI blog by Nurein Umeya.",
    description: "Machine Learning, AI, Engineering, Computer Science...",
};

export default function RootLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <html
            lang="en"
            className={`${geistSans.variable} ${geistMono.variable} h-full antialiased`}
        >
            <body className="min-h-full min-w-full w-full h-full flex flex-col justify-between">
                <header className="basis-1 grow-0 shrink-0 p-12">
                    <Home />

                </header>
                <main className="min-w-full w-full text-center py-10 px-10 basis-[80%] grow shrink-0">
                    {children}
                </main>
                <footer className="bg-black text-white p-5 pl-10 basis-[10%] grow-0 shrink-0 font-mono" style={{ minHeight: '100px', width: "100%" }}>
                    <a href={'https://nureinumeya.vercel.app'}>About me</a>
                    <span> | </span>
                    <Link href={'mailto:nurein.umeya@alumni.utoronto.ca'}>Contact</Link>
                </footer>
            </body>

        </html>
    );
}
