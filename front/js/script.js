document.addEventListener("DOMContentLoaded", function() {
    // Cridem a l'endpoint de l'API fent un fetch

    fetch("http://127.0.0.1:8000/alumnes/list")
///alumnes/list?contain=Luis
///alumnes/list?skip=2&limit=10     
////alumnes/list?orderby=asc
///alumnes/list
        .then(response => {
            if (!response.ok) {
                throw new Error("Error a la resposta del servidor");
            }
            return response.json();
        })
        .then(data => {
            const alumnesTableBody = document.querySelector("#tablaAlumne tbody");
            alumnesTableBody.innerHTML = ""; // Netejar la taula abans d'afegir res
            
            // Iterar sobre los alumnos y agregarlos al DOM
            data.forEach(alumne => {
                const row = document.createElement("tr");

                // const idCell = document.createElement("td");
                // idCell.textContent = alumne.IdAlumne;
                // row.appendChild(idCell); 

                // Repetir per tots els altres camps restants que retorna l'endpoint
            
                const NomCell = document.createElement("td");
                NomCell.textContent = alumne.NomAlumne;
                row.appendChild(NomCell);

                const CicleCell  = document.createElement("td");
                CicleCell .textContent = alumne.Cicle ;
                row.appendChild(CicleCell);

                const CursCell   = document.createElement("td");
                CursCell  .textContent = alumne.Curs;
                row.appendChild(CursCell );

                const grupCell = document.createElement("td");
                grupCell.textContent = alumne.Grup;
                row.appendChild(grupCell);

                const DesCell = document.createElement("td");
                DesCell.textContent = alumne.DescAula;
                row.appendChild(DesCell);

                alumnesTableBody.appendChild(row);
            });
        })
        .catch(error => {
            console.error("Error capturat:", error);
            alert("Error al carregar la llista d'alumnes");
        });
});