import { App } from "@/components/App";

export default async function Page({ params }: { params: Promise<{ group_id: string }> }) {
  const { group_id } = await params;
  return <App initialGroupId={group_id} />;
}
