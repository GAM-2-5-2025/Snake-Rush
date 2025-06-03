# Snake-Rush

# **PROŽDRLJIVA ZMIJA – McDonald's verzija**

## **Uvod**

“Proždrljiva zmija” je modernizirana verzija klasične igre Snake, nastala kao zajednički projekt troje učenika: Petre, Adriana i Eme. Temeljna ideja bila je stvoriti zabavnu i vizualno atraktivnu verziju igre s temom popularnog fast food lanca McDonald's, uz dodavanje novih funkcionalnosti kao što su početni zaslon, pauza, završni ekran i kontrolni gumbi. Igra je izrađena u Python programskom jeziku koristeći knjižnicu Pygame, s ciljem usavršavanja znanja o programiranju igara, radu s grafikom i timskoj suradnji.

## **Detaljan opis rada**

Igra se sastoji od više povezanih dijelova:

### **1. Početni zaslon (Start screen)**

Prije početka igre prikazuje se zaslon dobrodošlice s naslovom “PROŽDRLJIVA ZMIJA” i gumbom “POČETAK”. Klikom na gumb igra započinje.

### **2. Glavna igra**

* **Zmija** se sastoji od glave, tijela i repa, koji su prikazani različitim McDonald's slikama (npr. hamburgeri, sokovi, krumpirići).
* **Hrana** se generira nasumično na ekranu, a svaki pojeden objekt povećava rezultat za 10 bodova i produžuje zmiju. Hrana je prikazana slikama poput hamburgera, pomfrita i sladoleda.
* **Kretanje zmije** odvija se pomoću tipki sa strelicama na tipkovnici.
* **Pause gumb** (u gornjem desnom kutu) omogućuje zaustavljanje igre i nastavak kasnije.

### **3. Pauziranje (Pause screen)**

Kada igrač klikne na ikonu pauze, igra se zamrzava, ekran se zatamni i pojavljuje se natpis “PAUZA” s gumbom “NASTAVI”.

### **4. Završni zaslon (Game Over screen)**

Ako zmija udari u zid ili samu sebe, igra završava. Na ekranu se prikazuje postignuti broj bodova te gumbi “KRAJ” i “PONOVI”, što omogućuje igraču da izađe iz igre ili pokuša ponovno.

### **5. Bodovanje**

Trenutni rezultat prikazuje se u gornjem lijevom kutu ekrana tijekom cijele igre.

## **Tehničke informacije**

* **Programski jezik**: Python
* **Knjižnica**: Pygame
* **Rezolucija prozora**: 720x480 piksela
* **Veličina zmije i hrane**: 20x20 piksela
* **Brzina zmije**: 10 jedinica po frameu
* **Grafika**: Vlastite McDonald's slike (hamburger, kola, pomfrit, sladoled, itd.) koje se koriste kao hrana u igri i kao dijelovi tijela zmije.
* **Kontrole**: Tipkovnica (strelice) i miš (gumbi).
* **Potrebna sistemska konfiguracija**:

  * Operativni sustav: Windows/Linux/MacOS
  * Instalirani Python (verzija 3.8 ili novija)
  * Instalirana Pygame knjižnica
  * Minimalno 4 GB RAM-a

## **Izvorni kod**

Kompletan Python kod nalazi se u priloženoj `.py` datoteci. Uz kod, priložene su i sve slike korištene u igri (hamburger.png, kola.png, pomfrit.png, happymeal.png, chickenbox.png, sladoled.png, head.jpg.png, body.jpg.png, tail.jpg.png, zmija.png, pauza.png), te screencast datoteka.


