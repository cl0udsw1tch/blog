import Image from "next/image";
import Link from "next/link";

const papers = [
    { name: 'Backpropogation using Tensors', route: "/tensor-backprop" },
    { name: "A Steady State Incompressible Fluid Flow Solver using the SIMPLE method", route: "/fluid-flow-solver" }
]
export default function Home() {
    return (

        <div >

            <div className="border-b-gray-300 border-b-2" style={{ height: '100px' }}>
                <h1 className="text-3xl" >Articles</h1>
                <h2>Nurein Umeya</h2>
            </div >
            <ul style={{ listStyleType: 'circle', padding: '10px' }} >
                {papers.map((v) => <li style={{ textAlign: 'start' }} key={v.name}>
                    <Link href={v.route} >
                        {v.name}
                    </Link>
                </li>)}
            </ul>

        </div>

    );
}
