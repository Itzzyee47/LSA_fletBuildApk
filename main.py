import flet as ft

def main(page: ft.Page): 
    page.padding = 0
    
     
    wv = ft.WebView(
        "https://landmarkai.onrender.com/",
        width=500,height=650,
        on_page_started=lambda _: print("Page started"),
        on_page_ended=lambda _: print("Page ended"),
        on_web_resource_error=lambda e: print("Page error:", e.data),
    )
    sa = ft.SafeArea(content=wv,)
    page.add(sa,)

ft.app(main)
