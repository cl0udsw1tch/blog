
'use client'
import { useState } from "react"
import Link from "next/link"

const scaleHover = 1.2

const Home = () => {
    const [scale, setScale] = useState(1)
    return (
        <Link href={"/"} onMouseOver={(e) => setScale(prev => scaleHover)} onMouseLeave={(e) => { setScale((prev) => 1) }} style={{ transform: `scale(${scale})`, display: 'inline-block' }}> home</Link >
    )
}

export default Home


