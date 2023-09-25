# Karse

Kode brukt i forskningsoppgaven om karse og energidrikker.

For å utføre målingene til dette eksperimentet har vi brukt to python-program, et for kamera og et for lysmåler. Biblioteket “cv2” er brukt for å ta og lagre bilder, “time” for å ha et program som starter og stopper, “datetime” for å lagre dagens dato med bildet og med lysmålingen, og “labquest” for å hente ut data fra labquesten.

Kameraprogrammet (camer.py) tar et bilde hvert tiende minutt og lagrer dette med navn “image” og dato i formatet  “dag time minutt sekund”. 
Lysmåleprogrammet (main.py) starter labquesten med en datainnsamlingsperiode på 4 sekunder, kjører om og om igjen at den legger til dato og data i et txt dokument en gang og så venter et minutt før den gjentar. Når man avslutter programmet stanses labquesten.
