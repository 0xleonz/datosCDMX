#import "curp/datos.typ": *

#set page(paper: "a4", margin: 1in)
#set text(size: 12pt, weight: 400)
#set par(justify: true, leading: 0.9em)

// Para figuras alineadas a la izquierda
#show figure.caption: it => {
  set align(left)
  it
}
#show link: underline


// Contents
#set page(numbering: "i")
#counter(page).update(1)

// Main matter
// #set par(first-line-indent: 2em)
#set par(spacing: 1.6em)
#set page(numbering: "1")
#counter(page).update(1)


#text(30pt)[Ejercicios por Edgar Mendoza León]

#set heading(numbering: "1.")
#outline(title: "Índice")
#include "ejercicios/reporte1.typ"
#include "ejercicios/reporte2.typ"
#include "ejercicios/reporte3.typ"
#include "ejercicios/reporte4.typ"

#pagebreak()
#bibliography("assets/references.yml", title: "Referencias")
