
  //progress_bar
  var bar = document.querySelector('#pone'),
                                numberTop_bar = bar.getBoundingClientRect().top,
                                start = +bar.innerHTML, end = +bar.dataset.max;

                            window.addEventListener('scroll', function onScroll() {
                                if (window.pageYOffset > numberTop_bar - window.innerHeight / 2) {
                                    this.removeEventListener('scroll', onScroll);
                                    var elem = document.getElementById("pone");
                                    var width = 0;
                                    var endwidth = 100;
                                    var id = setInterval(frame_bar, 10);
                                    function frame_bar() {
                                        if (width >= endwidth) {
                                            clearInterval(id);
                                        } else {
                                            width++;
											elem.style.backgroundColor = '#325dac'
                                            elem.style.width = width + '%';
											if (width==100)
											{
											elem.innerHTML = '<span id="test" >' +  334 + ' земли' + '</span>';
											var op = document.getElementById("test");
											//op.style.opacity = 0;
											//op.id.style = 
											//op.style.transition = 'opacity 5s ease';
											//op.style.opacity = 1;
											}
                                        }
                                    }

                                }
                            });
  