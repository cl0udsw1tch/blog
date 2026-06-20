import PaperPage from "./PaperPage";

export default async function page({
    params,
}: {
    params: Promise<{ slug: string }>;
}) {
    const { slug } = await params;

    return (
        <main className="page paper">
            <PaperPage page={slug} />
        </main>
    )



}
