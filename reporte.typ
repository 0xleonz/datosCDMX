#import "curp/datos.typ": *

#set page(paper: "a4", margin: 1in)
#set text(size: 12pt, weight: 400)
#set par(justify: true, leading: 0.9em)

#show heading.where(level: 1): it => (
  pagebreak(to: "odd") +
  block(width: 100%, below: 1.8em)[
    #set align(center)
    #set text(24pt)
   #it.body])
#show heading.where(level: 2): it => (
  v(10pt) +
  block(width: 100%, above: 1.3em, below: 1.5em)[
    #set align(center)
    #set text(15pt)
    #it.body])
#show heading.where(level: 3): it => (
  v(8pt) +
  block(width: 100%, above: 1em, below: 1em)[
    #set text(11pt)
    #it.body])

// Para figuras alineadas a la izquierda
#show figure.caption: it => {
  set align(left)
  it
}



// Contents
#set page(numbering: "i")
#counter(page).update(1)

// Main matter
// #set par(first-line-indent: 2em)
#set par(spacing: 1.6em)
#set page(numbering: "1")
#counter(page).update(1)


#set heading(numbering: "1.")
#outline(title: "Índice")
#include "ejercicios/reporte1.typ"
#include "ejercicios/reporte2.typ"
#include "ejercicios/reporte4.typ"
