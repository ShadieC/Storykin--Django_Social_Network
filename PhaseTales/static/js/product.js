const closeFun= ()=>{
      let modelBox = document.getElementById("ModelBox");
  
  modelBox.classList.remove("open");
  modelBox.classList.add("close");
}

const openFun= ()=>{
      let modelBox = document.getElementById("ModelBox");
  
  modelBox.classList.remove("close");
  modelBox.classList.add("open");
}

 //-----------

const openPost= ()=>{
      let modelBox = document.getElementById("Post_ModalBox");
  
  modelBox.classList.remove("close");
  modelBox.classList.add("open");
}

const closePost= ()=>{
      let modelBox = document.getElementById("Post_ModalBox");
  
  modelBox.classList.remove("open");
  modelBox.classList.add("close");
}

 //-----------

const openCreatePost= ()=>{
      let modelBox = document.getElementById("Create_Post");
      let error = document.getElementById("floating-post-error");
  
  modelBox.classList.remove("close");
  modelBox.classList.add("open");
  error.classList.add('dissapear');
}

const closeCreatePost= ()=>{
      let modelBox = document.getElementById("Create_Post");
      let error = document.getElementById("floating-post-error");
  
  modelBox.classList.remove("open");
  modelBox.classList.add("close");
  error.classList.add('dissapear');
}

 //-----------

const openCreateQuestion= ()=>{
      let modelBox = document.getElementById("Create_Question");
      let error = document.getElementById("floating-question-error");
  
  modelBox.classList.remove("close");
  modelBox.classList.add("open");
  error.classList.add('dissapear');
}

const closeCreateQuestion= ()=>{
      let modelBox = document.getElementById("Create_Question");
      let error = document.getElementById("floating-question-error");
  
  modelBox.classList.remove("open");
  modelBox.classList.add("close");
  error.classList.add('dissapear');
}

 //-----------

const openPhases= ()=>{
      let modelBox = document.getElementById("Phases_ModalBox");
  
  modelBox.classList.remove("close");
  modelBox.classList.add("open");
}

const closePhases= ()=>{
      let modelBox = document.getElementById("Phases_ModalBox");
  
  modelBox.classList.remove("open");
  modelBox.classList.add("close");
}

const openCreateAnswer= ()=>{
      let modelBox = document.getElementById("Create_Answer");
      let error = document.getElementById("floating-question-answer-error");
  
  modelBox.classList.remove("close");
  modelBox.classList.add("open");
  error.classList.add('dissapear');
}

const closeCreateAnswer= ()=>{
      let modelBox = document.getElementById("Create_Answer");
      let error = document.getElementById("floating-question-answer-error");
  
  modelBox.classList.remove("open");
  modelBox.classList.add("close");
  error.classList.add('dissapear');
}

const openReply= ()=>{
      let modelBox = document.getElementById("Reply_ModalBox");
  
  modelBox.classList.remove("close");
  modelBox.classList.add("open");
}

const closeReply= ()=>{
      let modelBox = document.getElementById("Reply_ModalBox");
  
  modelBox.classList.remove("open");
  modelBox.classList.add("close");
}

const openRegistration= ()=>{
      let modelBox = document.getElementById("Registration_ModalBox");
  
  modelBox.classList.remove("close");
  modelBox.classList.add("open");
}

const closeRegistration= ()=>{
      let modelBox = document.getElementById("Registration_ModalBox");
  
  modelBox.classList.remove("open");
  modelBox.classList.add("close");
}