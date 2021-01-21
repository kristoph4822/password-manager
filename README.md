Przy pierwszym uruchomieniu kontener z aplikacją (flask) trzeba ręcznie zrestartować. 
Aplikacja nie może od razu się połączyć z bazą danych, ponieważ utworzenie tabel w MySQL zajmuje trochę czasu, co wywołuje błąd.

Restart poleceniem:

    docker restart flask