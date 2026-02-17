import "./globals.css";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Social Manager",
  description: "Piattaforma per pianificare e monitorare i contenuti social"
};

export default function RootLayout({
  children
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="it">
      <body>{children}</body>
    </html>
  );
}
