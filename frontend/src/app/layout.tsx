import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Model Scout",
  description: "한국어 모델·데이터셋 추천",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="ko">
      <body className="antialiased">{children}</body>
    </html>
  );
}
