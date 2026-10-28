"use client";

import ImmersiveFullscreenNav from "@/components/ui/immersive-full-screen-nav";

export default function ImmersiveFullscreenNavDemo() {
  return (
    <div className="w-full min-w-0 bg-[#0d1823] text-white">
      <ImmersiveFullscreenNav
        navConfig={{
          brand: "SIF-INTEL",
          brandHref: "#",
          overlayBg: "#0d1823",
          clipOrigin: "left",
          headerOpenColor: "#6bc8ff",
        }}
        navContent={{
          agencyName: "Industrial Safety Intelligence",
          tagline: "Autonomous Sentinel AI for High-Risk Environments",
          location: "Plant 04 · Autonomous HUD",
          links: [
            { label: "Live Telemetry", href: "#" },
            { label: "Hazard Matrix", href: "#" },
            { label: "CCTV Feeds", href: "#" },
            { label: "Emergency Interlocks", href: "#" },
          ],
          images: [
            "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=800&q=80",
          ],
          socials: [
            { type: "instagram", href: "#" },
            { type: "twitter", href: "#" },
            { type: "linkedin", href: "#" },
          ],
        }}
      />

      <main className="flex h-screen flex-col items-center justify-center gap-4 bg-[#0d1823] px-6 text-center text-white">
        <p className="text-xs uppercase tracking-[0.3em] text-[#6bc8ff]">Safety System Navigation</p>
        <h1 className="max-w-2xl text-[7vw] font-bold leading-tight max-md:text-[9vw]">
          Autonomous Sentinel HUD
        </h1>
        <p className="mt-2 max-w-md text-sm leading-relaxed text-slate-400">
          Click the upper-right menu button to reveal full-screen clip-path spatial navigation with real-time industrial telemetry channels.
        </p>
      </main>
    </div>
  );
}
