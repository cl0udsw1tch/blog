export interface PaperMeta {
    slug: string;
    title: string;
    date: string;
    category: string;
    description: string;
    file: string;
    type: string;
}

export const papers: PaperMeta[] = [
    {
        slug: "tensors-II",
        title: "Tensors II: Universality",
        date: "2026-06-17",
        category: "Math",
        description: "",
        file: "tensors-II.html",
        type: "html",
    },
    {
        slug: "tensors-I",
        title: "Tensors I: Construction",
        date: "2026-06-10",
        category: "Math",
        description: "",
        file: "tensors-I.html",
        type: "html",

    },
    {
        slug: "backpropogation-using-tensors",
        title: "Backpropogation using Tensors",
        date: "2026-06-10",
        category: "Machine Learning",
        description: "",
        file: "tensor-backprop.html",
        type: "html",

    },
    {
        slug: "SIMPLE-fluid-solver",
        title: "A Steady State Incompressible Fluid Flow Solver using the SIMPLE method",
        date: "2026-06-10",
        category: "Engineering",
        description: "",
        file: "fluid-flow-solver.pdf",
        type: "pdf",

    }
];
