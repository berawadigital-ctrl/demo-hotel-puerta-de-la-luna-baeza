# Contenido de la demo Hotel Puerta de la Luna (Baeza) (es/en/fr/de). Hechos de hotelpuertadelaluna.com leidos el 02/11/2026 (ver berawa/sources.json). Sin precios (ni de habitaciones ni de menus), sin valoraciones, porcentajes ni reseñas; sin nombres de personas.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el hotel real.','en':' Images are illustrations and do not show the actual hotel.','fr':' Les images sont des illustrations et ne montrent pas l’hôtel réel.','de':' Die Bilder sind Illustrationen und zeigen nicht das tatsächliche Hotel.'}
H={'es':['Habitaciones','Suites y opciones para familias'],'en':['Rooms','Suites and family options'],'fr':['Chambres','Suites et options familles'],'de':['Zimmer','Suiten und Familienoptionen']}
RD={
'es':['Business, standard, standard con cama extragrande, superior con vistas, premium con terraza, deluxe con salón y triple. Cada una decorada de forma individual.','Suite con vistas y suite familiar con vistas y terraza, hasta 4 huéspedes. También dos habitaciones dobles contiguas para tres, cuatro o cinco personas.'],
'en':['Business, standard, standard with extra-large bed, superior with views, premium with terrace, deluxe with lounge and triple. Each one individually decorated.','Suite with views and family suite with views and terrace, up to 4 guests. Also two adjoining double rooms for three, four or five people.'],
'fr':['Business, standard, standard avec lit très grand, supérieure avec vue, premium avec terrasse, deluxe avec salon et triple. Chacune décorée de façon individuelle.','Suite avec vue et suite familiale avec vue et terrasse, jusqu’à 4 personnes. Aussi deux chambres doubles contiguës pour trois, quatre ou cinq personnes.'],
'de':['Business, Standard, Standard mit extragroßem Bett, Superior mit Aussicht, Premium mit Terrasse, Deluxe mit Salon und Dreibettzimmer. Jedes individuell eingerichtet.','Suite mit Aussicht und Familiensuite mit Aussicht und Terrasse, bis 4 Gäste. Außerdem zwei nebeneinanderliegende Doppelzimmer für drei, vier oder fünf Personen.']}
ART={
'hero':('arches',7611,['#171a22','#b99a5f','#ede0c2','#5b5444','#3c382f','#1f1e1c']),
'intro':('columns',7612,['#f3efe6','#faf8f1','#8a7346','#5c4e34','#2a251b']),
'r1':('arches',7621,['#eee9de','#cdb07a','#8a7346','#5c4e34','#2a251b']),
'r2':('columns',7622,['#171a22','#c4a66c','#efe3c8','#665d4b','#433e33','#22201d']),
'g1':('hills',7631,['#ebe6da','#efe4cb','#cdb07a','#9e9270','#716851','#4a4537']),
'g2':('skyline',7632,['#171a22','#b99a5f','#ede0c2','#5b5444','#3c382f','#1f1e1c']),
'g3':('waves',7633,['#f1ece2','#f9f6ee','#97804f','#5c4e34','#2a251b']),
'g4':('arches',7634,['#171a22','#c4a66c','#efe3c8','#665d4b','#433e33','#22201d'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Puerta de la Luna · Hotel con encanto en Baeza',see_rooms='Ver las habitaciones',hero_k='Baeza · C. Canónigo Melgares Raya, 7',hero_t='Una mansión del siglo XVI en el corazón de Baeza',hero_s='Hotel boutique a escasos 50 metros de la catedral, con piscina, jardines y restaurante gastronómico.',
 intro_t='Hotel con encanto en Baeza',intro_p1='El hotel ocupa una hermosa mansión del siglo XVI en el casco antiguo de Baeza, ciudad Patrimonio de la Humanidad. Cada habitación está decorada de forma individual.',
 intro_p2='Cuenta con piscina al aire libre, jardines, el Restaurante Acebuche, con cocina de autor y menús degustación, y el Bar Pacos, de raciones típicas de la zona.',
 stats=['A 50 m de la catedral','Piscina exterior en verano','Parking privado','Restaurante Acebuche'],nav_rooms='Habitaciones',rooms_t='Habitaciones y suites',rooms_s='Todas con aire acondicionado, wifi gratuito, minibar y productos de cortesía.',
 svcs=['Piscina exterior en temporada de verano','Parking privado','Restaurante Acebuche','Bar Pacos','Visitas guiadas','Salones para convenciones y celebraciones'],
 loc_p='C. Canónigo Melgares Raya, 7 · 23440 Baeza (Jaén). Teléfono: 953 74 70 19. Correo: informacionyreservas@hotelpuertadelaluna.com.',
 chips=['¿Qué habitaciones tenéis?','¿Hay piscina?','¿Hay restaurante?','¿Cómo reservo?']),
'en':dict(title='Hotel Puerta de la Luna · Charming hotel in Baeza',see_rooms='See the rooms',hero_k='Baeza · C. Canónigo Melgares Raya, 7',hero_t='A 16th-century mansion in the heart of Baeza',hero_s='Boutique hotel just 50 metres from the cathedral, with pool, gardens and a gastronomic restaurant.',
 intro_t='Charming hotel in Baeza',intro_p1='The hotel occupies a beautiful 16th-century mansion in the old town of Baeza, a World Heritage city. Each room is individually decorated.',
 intro_p2='It has an outdoor pool, gardens, the Acebuche Restaurant, with signature cuisine and tasting menus, and Bar Pacos, serving typical local dishes.',
 stats=['50 m from the cathedral','Outdoor pool in summer','Private parking','Acebuche Restaurant'],nav_rooms='Rooms',rooms_t='Rooms and suites',rooms_s='All with air conditioning, free wifi, minibar and complimentary toiletries.',
 svcs=['Outdoor pool in summer season','Private parking','Acebuche Restaurant','Bar Pacos','Guided tours','Convention and celebration halls'],
 loc_p='C. Canónigo Melgares Raya, 7 · 23440 Baeza (Jaén). Phone: +34 953 74 70 19. Email: informacionyreservas@hotelpuertadelaluna.com.',
 chips=['Which rooms do you have?','Is there a pool?','Is there a restaurant?','How do I book?']),
'fr':dict(title='Hôtel Puerta de la Luna · Hôtel de charme à Baeza',see_rooms='Voir les chambres',hero_k='Baeza · C. Canónigo Melgares Raya, 7',hero_t='Une demeure du XVIe siècle au cœur de Baeza',hero_s='Hôtel boutique à 50 mètres de la cathédrale, avec piscine, jardins et restaurant gastronomique.',
 intro_t='Hôtel de charme à Baeza',intro_p1='L’hôtel occupe une belle demeure du XVIe siècle dans la vieille ville de Baeza, ville du patrimoine mondial. Chaque chambre est décorée de façon individuelle.',
 intro_p2='Il dispose d’une piscine extérieure, de jardins, du restaurant Acebuche, cuisine d’auteur et menus dégustation, et du Bar Pacos, avec des plats typiques de la région.',
 stats=['À 50 m de la cathédrale','Piscine extérieure en été','Parking privé','Restaurant Acebuche'],nav_rooms='Chambres',rooms_t='Chambres et suites',rooms_s='Toutes avec climatisation, wifi gratuit, minibar et produits d’accueil.',
 svcs=['Piscine extérieure en été','Parking privé','Restaurant Acebuche','Bar Pacos','Visites guidées','Salons pour congrès et célébrations'],
 loc_p='C. Canónigo Melgares Raya, 7 · 23440 Baeza (Jaén). Téléphone : +34 953 74 70 19. E-mail : informacionyreservas@hotelpuertadelaluna.com.',
 chips=['Quelles chambres avez-vous ?','Y a-t-il une piscine ?','Y a-t-il un restaurant ?','Comment réserver ?']),
'de':dict(title='Hotel Puerta de la Luna · Charmantes Hotel in Baeza',see_rooms='Zimmer ansehen',hero_k='Baeza · C. Canónigo Melgares Raya, 7',hero_t='Ein Herrenhaus aus dem 16. Jahrhundert im Herzen von Baeza',hero_s='Boutique-Hotel nur 50 Meter von der Kathedrale, mit Pool, Gärten und Gourmetrestaurant.',
 intro_t='Charmantes Hotel in Baeza',intro_p1='Das Hotel befindet sich in einem schönen Herrenhaus aus dem 16. Jahrhundert in der Altstadt von Baeza, einer Welterbestadt. Jedes Zimmer ist individuell eingerichtet.',
 intro_p2='Es gibt einen Außenpool, Gärten, das Restaurant Acebuche mit Autorenküche und Degustationsmenüs sowie die Bar Pacos mit typischen Gerichten der Region.',
 stats=['50 m von der Kathedrale','Außenpool im Sommer','Privatparkplatz','Restaurant Acebuche'],nav_rooms='Zimmer',rooms_t='Zimmer und Suiten',rooms_s='Alle mit Klimaanlage, kostenlosem WLAN, Minibar und Pflegeprodukten.',
 svcs=['Außenpool in der Sommersaison','Privatparkplatz','Restaurant Acebuche','Bar Pacos','Führungen','Säle für Tagungen und Feiern'],
 loc_p='C. Canónigo Melgares Raya, 7 · 23440 Baeza (Jaén). Telefon: +34 953 74 70 19. E-Mail: informacionyreservas@hotelpuertadelaluna.com.',
 chips=['Welche Zimmer gibt es?','Gibt es einen Pool?','Gibt es ein Restaurant?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
RE='https://hotelpuertadelaluna.booking-channel.com/disponibilidad.html';RN='https://hotelpuertadelaluna.booking-channel.com/EN/availability.html'
BOOK=dict(mode='engine',url=dict(es=RE,en=RN,fr=RN,de=RN))
D=dict(name='Hotel Puerta de la Luna',ac='#1b1d26',ac2='#8a7346',ac2_a11y='#6a5733',book=BOOK,around=[],foot=FOOT,
 address='C. Canónigo Melgares Raya, 7 · 23440 Baeza (Jaén)',phones=['+34 953 74 70 19'],emails=['informacionyreservas@hotelpuertadelaluna.com'],maps='Hotel Puerta de la Luna, Calle Canónigo Melgares Raya 7, 23440 Baeza',t=T)
META=dict(repo='demo-hotel-puerta-de-la-luna-baeza',name='Hotel Puerta de la Luna',legal_name='Hotel Acebuche S.L., CIF B23431760 (aviso legal de su web)',registry_ids=['B23431760'],
 url='https://www.hotelpuertadelaluna.com/',domain='hotelpuertadelaluna.com',municipality='Baeza',province='Jaén',sector='hotel con encanto en una mansion del siglo XVI en el casco antiguo de Baeza',
 read_at='2026-11-02T07:23:00+01:00',created_at='2026-11-02T07:22:00+01:00',built_at='2026-11-02T07:32:00+01:00',audit_date='2026-11-02T07:22:00+01:00',
 rating=dict(value=4.4,coincide=['tel','web'],date='2026-10-29',url='https://www.google.com/maps/place/Puerta+de+La+Luna+%7C+Hotel+Baeza/@37.9898634,-3.4697906,17z'),
 book=dict(mode='engine',url=RE,note='motor booking-channel enlazado desde su web: disponibilidad.html (es) y EN/availability.html (en; el motor solo tiene ES y EN, se usa EN para fr/de). HTTP 200 los dos (02/11/2026 07:22).'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Tenéis suites?','K02'),('Viajamos en familia, ¿qué opciones hay?','K03'),('¿Hay wifi?','K04'),('¿Hay piscina?','K05'),('¿Hay parking?','K06'),('¿Hay restaurante?','K07'),('¿Dónde se pueden tomar tapas?','K08'),('¿Dónde estáis?','K09'),('¿Cómo reservo?','K10'),('¿Podéis confirmarme disponibilidad para mañana?','K10'),('¿Organizáis bodas?','K11'),('¿Cuál es vuestro teléfono?','K12'),('¿Hacéis visitas guiadas?','K13'),('¿Cuánto cuesta la noche?',None),('¿Tenéis campo de golf?',None)],
'en':[('Which rooms do you have?','K01'),('Do you have suites?','K02'),('We are a family, what options are there?','K03'),('Is there wifi?','K04'),('Is there a pool?','K05'),('Is there parking?','K06'),('Is there a restaurant?','K07'),('Where can I have tapas?','K08'),('Where are you?','K09'),('How do I book?','K10'),('Can you confirm availability for tomorrow?','K10'),('Do you host weddings?','K11'),('What is your phone number?','K12'),('Do you offer guided tours?','K13'),('How much is a night?',None),('Do you have a golf course?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Avez-vous des suites ?','K02'),('Nous voyageons en famille, quelles options ?','K03'),('Y a-t-il le wifi ?','K04'),('Y a-t-il une piscine ?','K05'),('Y a-t-il un parking ?','K06'),('Y a-t-il un restaurant ?','K07'),('Où peut-on manger des tapas ?','K08'),('Où êtes-vous ?','K09'),('Comment réserver ?','K10'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K10'),('Organisez-vous des mariages ?','K11'),('Quel est votre numéro de téléphone ?','K12'),('Proposez-vous des visites guidées ?','K13'),('Combien coûte la nuit ?',None),('Avez-vous un terrain de golf ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Haben Sie Suiten?','K02'),('Wir reisen als Familie, welche Optionen gibt es?','K03'),('Gibt es WLAN?','K04'),('Gibt es einen Pool?','K05'),('Gibt es Parkplätze?','K06'),('Gibt es ein Restaurant?','K07'),('Wo gibt es Tapas?','K08'),('Wo liegt das Hotel?','K09'),('Wie kann ich buchen?','K10'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K10'),('Richten Sie Hochzeiten aus?','K11'),('Wie ist Ihre Telefonnummer?','K12'),('Bieten Sie Führungen an?','K13'),('Was kostet eine Nacht?',None),('Haben Sie einen Golfplatz?',None)]}
