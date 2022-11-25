function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }


function editNote(noteId) {
  console.log(noteId);

  var noteData = document.getElementById('edit_note'+noteId).value;

  fetch("/edit-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId, noteData : noteData}),
  }).then((_res) => {
    window.location.href = "/";
  });
}


function sortList() {
  var list, i, switching, b, shouldSwitch;
  list = document.getElementById("notes");
  switching = true;
  console.log("Hallo")
  //notes = user.notes;

  while (switching) {
    // Start by saying: no switching is done:
    switching = false;
    b = list.getElementsByTagName("LI");
    // Loop through all list items:
    for (i = 0; i < (b.length - 1); i++) {
      // Start by saying there should be no switching:
      shouldSwitch = false;
      /* Check if the next item should
      switch place with the current item: */



      if (b[i].innerHTML.toLowerCase() > b[i + 1].innerHTML.toLowerCase()) {
        /* If next item is alphabetically lower than current item,
        mark as a switch and break the loop: */
        shouldSwitch = true;
        break;
      }
    }
    if (shouldSwitch) {
      /* If a switch has been marked, make the switch
      and mark the switch as done: */
      b[i].parentNode.insertBefore(b[i + 1], b[i]);
      switching = true;
    }
  }
}

