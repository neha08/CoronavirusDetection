(function($) {

	"use strict";

	var fullHeight = function() {

		$('.js-fullheight').css('height', $(window).height());
		$(window).resize(function(){
			$('.js-fullheight').css('height', $(window).height());
		});

	};
	fullHeight();

	$('#sidebarCollapse').on('click', function () {
      $('#sidebar').toggleClass('active');
  });

})(jQuery);


		function toggleClass(elem,className){
		  if (elem.className.indexOf(className) !== -1){
		    elem.className = elem.className.replace(className,'');
		  }
		  else{
		    elem.className = elem.className.replace(/\s+/g,' ') + 	' ' + className;
		  }
		  return elem;
		}

		function toggleDisplay(elem){
		  const curDisplayStyle = elem.style.display;			
		  if (curDisplayStyle === 'none' || curDisplayStyle === ''){
		    elem.style.display = 'block';
		  }
		  else{
		    elem.style.display = 'none';
		  }
		}

		function toggleMenuDisplay(e){
		  const dropdown = e.currentTarget.parentNode;
		  const menu = dropdown.querySelector('.menu');
		  const icon = dropdown.querySelector('.fa-angle-right');
		  toggleClass(menu,'hide');
		  toggleClass(icon,'rotate-90');
		}

		function handleOptionSelected(e){
		  toggleClass(e.target.parentNode, 'hide');			
		  const id = e.target.id;
		  const newValue = e.target.textContent + ' ';
		  const titleElem = document.querySelector('.dropdown .title');
		  const icon = document.querySelector('.dropdown .title .fa');
		  titleElem.textContent = newValue;
		  titleElem.appendChild(icon);
		  //trigger custom event
		  document.querySelector('.dropdown .title').dispatchEvent(new Event('change'));
		    //setTimeout is used so transition is properly shown
		  setTimeout(() => toggleClass(icon,'rotate-90',0));
		}

		function handleTitleChange(e){
		  const result = document.getElementById('result');
		  result.innerHTML = 'The result is: ' + e.target.textContent;
		}

		function handleOptionSelected2(e){	
		  toggleClass(e.target.parentNode, 'hide');			
		  const id = e.target.id;
		  const newValue = e.target.textContent + ' ';
		  const titleElem = document.querySelector('.dropdown2 .title2');
		  const icon = document.querySelector('.dropdown2 .title2 .fa');
		  titleElem.textContent = newValue;
		  titleElem.appendChild(icon);
		  //trigger custom event
		  document.querySelector('.dropdown2 .title2').dispatchEvent(new Event('change'));
		    //setTimeout is used so transition is properly shown
		  setTimeout(() => toggleClass(icon,'rotate-90',0));
		}

		function handleTitleChange2(e){
		  const result = document.getElementById('result2');
		  result.innerHTML = 'The result is: ' + e.target.textContent;
		}

		function toggleMenuDisplay2(e){
		  const dropdown = e.currentTarget.parentNode;
		  const menu = dropdown.querySelector('.menu2');
		  const icon = dropdown.querySelector('.fa-angle-right');

		  toggleClass(menu,'hide');
		  toggleClass(icon,'rotate-90');
		}

		function handleOptionSelected3(e){	
		  toggleClass(e.target.parentNode, 'hide');			
		  const id = e.target.id;
		  const newValue = e.target.textContent + ' ';
		  const titleElem = document.querySelector('.dropdown3 .title3');
		  const icon = document.querySelector('.dropdown3 .title3 .fa');
		  titleElem.textContent = newValue;
		  titleElem.appendChild(icon);
		  //trigger custom event
		  document.querySelector('.dropdown3 .title3').dispatchEvent(new Event('change'));
		    //setTimeout is used so transition is properly shown
		  setTimeout(() => toggleClass(icon,'rotate-90',0));
		}

		function handleTitleChange3(e){
		  const result = document.getElementById('result3');
		  result.innerHTML = 'The result is: ' + e.target.textContent;
		}

		function toggleMenuDisplay3(e){
		  const dropdown = e.currentTarget.parentNode;
		  const menu = dropdown.querySelector('.menu3');
		  const icon = dropdown.querySelector('.fa-angle-right');

		  toggleClass(menu,'hide');
		  toggleClass(icon,'rotate-90');
		}

		function handleOptionSelected4(e){	
		  toggleClass(e.target.parentNode, 'hide');			
		  const id = e.target.id;
		  const newValue = e.target.textContent + ' ';
		  const titleElem = document.querySelector('.dropdown4 .title4');
		  const icon = document.querySelector('.dropdown4 .title4 .fa');
		  titleElem.textContent = newValue;
		  titleElem.appendChild(icon);
		  //trigger custom event
		  document.querySelector('.dropdown4 .title4').dispatchEvent(new Event('change'));
		    //setTimeout is used so transition is properly shown
		  setTimeout(() => toggleClass(icon,'rotate-90',0));
		}

		function handleTitleChange4(e){
		  const result = document.getElementById('result4');
		  result.innerHTML = 'The result is: ' + e.target.textContent;
		}

		function toggleMenuDisplay4(e){
		  const dropdown = e.currentTarget.parentNode;
		  const menu = dropdown.querySelector('.menu4');
		  const icon = dropdown.querySelector('.fa-angle-right');

		  toggleClass(menu,'hide');
		  toggleClass(icon,'rotate-90');
		}
		//get elements
		const dropdownTitle = document.querySelector('.dropdown .title');
		const dropdownOptions = document.querySelectorAll('.dropdown .option');
		//bind listeners to these elements
		dropdownTitle.addEventListener('click', toggleMenuDisplay);
		dropdownOptions.forEach(option => option.addEventListener('click',handleOptionSelected));
		document.querySelector('.dropdown .title').addEventListener('change',handleTitleChange);

		//get elements
		const dropdownTitle2 = document.querySelector('.dropdown2 .title2');
		const dropdownOptions2 = document.querySelectorAll('.dropdown2 .option2');

		//bind listeners to these elements
		dropdownTitle2.addEventListener('click', toggleMenuDisplay2);
		dropdownOptions2.forEach(option2 => option2.addEventListener('click',handleOptionSelected2));
		document.querySelector('.dropdown2 .title2').addEventListener('change',handleTitleChange2);

		//get elements
		const dropdownTitle3 = document.querySelector('.dropdown3 .title3');
		const dropdownOptions3 = document.querySelectorAll('.dropdown3 .option3');
		//bind listeners to these elements
		dropdownTitle3.addEventListener('click', toggleMenuDisplay3);
		dropdownOptions3.forEach(option3 => option3.addEventListener('click',handleOptionSelected3));
		document.querySelector('.dropdown3 .title3').addEventListener('change',handleTitleChange3);

		//get elements
		const dropdownTitle4 = document.querySelector('.dropdown4 .title4');
		const dropdownOptions4 = document.querySelectorAll('.dropdown4 .option4');

		//bind listeners to these elements
		dropdownTitle4.addEventListener('click', toggleMenuDisplay4);
		dropdownOptions4.forEach(option4 => option4.addEventListener('click',handleOptionSelected4));
		document.querySelector('.dropdown4 .title4').addEventListener('change',handleTitleChange4);

