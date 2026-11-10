import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Model Scout",
  description: "한국어 모델·데이터셋 추천",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="ko">
      <body className="antialiased">
        {children}
        {process.env.NEXT_PUBLIC_API_URL?.startsWith("/api/mock") && (
          <div role="status" className="fixed bottom-3 right-3 z-[60] rounded-full bg-ink px-3 py-1.5 text-xs font-semibold text-white shadow">
            시연 데이터 · 실제 추천 결과가 아니에요
          </div>
        )}
      </body>
    </html>
  );
}
