'use client'
import { useState, useEffect } from "react"
export default function Page() {

    const [html, setHtml] = useState('')

    useEffect(() => {
        fetch('/tensor-backprop/index.html')
            .then(res => res.text())
            .then(res => setHtml(res))
    }, [])
    console.log(html)
    return (
        <div className="p-10 max-w-screen-lg text-left" dangerouslySetInnerHTML={{ __html: html }} style={{ fontFamily: 'var(--font-open-sans)' }}></div>
    )
}
