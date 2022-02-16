$(function () {
  var Accordion = function (el, multiple) {
    this.el = el || {};
    this.multiple = multiple || false;

    // Variables privadas
    var links = this.el.find('.link');
    // Evento
    links.on('click', { el: this.el, multiple: this.multiple }, this.dropdown);
  };

  Accordion.prototype.dropdown = function (e) {
    var $el = e.data.el;
    $this = $(this),
      $next = $this.next();

    $next.slideToggle();
    $this.parent().toggleClass('open');

    if (!e.data.multiple) {
      $el.find('.submenu').not($next).slideUp().parent().removeClass('open');
    };
  };

  var accordion = new Accordion($('#accordion'), false);
});
$(function () {
  var Accordion = function (el, multiple) {
    this.el = el || {};
    this.multiple = multiple || false;

    // Variables privadas
    var links = this.el.find('.link');
    // Evento
    links.on('click', { el: this.el, multiple: this.multiple }, this.dropdown);
  };

  Accordion.prototype.dropdown = function (e) {
    var $el = e.data.el;
    $this = $(this),
      $next = $this.next();

    $next.slideToggle();
    $this.parent().toggleClass('open');

    if (!e.data.multiple) {
      $el.find('.submenu').not($next).slideUp().parent().removeClass('open');
    };
  };

  var accordion = new Accordion($('#accordion-mobile'), false);
});

//number_change
const c = new countUp.CountUp("counter1", 1686, { separator: '&nbsp;' });
const d = new countUp.CountUp("counter2", 72, { separator: '&nbsp;' });
const e = new countUp.CountUp("counter3", 79, { separator: '&nbsp;' });


var number = document.querySelector('#counter1'),
  numberTop = number.getBoundingClientRect().top,
  start = +number.innerHTML, end = +number.dataset.max;

window.addEventListener('scroll', function onScroll() {
  if (window.pageYOffset > numberTop - window.innerHeight / 2) {
    this.removeEventListener('scroll', onScroll);
    c.start()
    d.start()
    e.start()
  }
});



//highcharts
  
Highcharts.chart('container', {
	chart: {
		type: 'line'
	},
	title: {
		text: 'График изменения цены в этом районе'
	},
	subtitle: {
		text: 'с 1 января 2020 по 31 декабря 2020'
	},
	xAxis: {
		categories: ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
	},
	yAxis: {
		title: {
			text: 'Цена в тыс. руб/сотку'
		}
	},
	plotOptions: {
		line: {
			dataLabels: {
				enabled: true
			},
			enableMouseTracking: false
		}
	},
	series: [{
		name: 'Цена',
		data: [700, 690, 950, 877, 765, 678, 689, 800, 831, 900, 899, 878]
	}, {
		name: 'Цена 2',
		data: [743, 656, 555, 678, 765, 678, 634, 844, 724, 900, 899, 878]
	},
	{
		name: 'Цена 3',
		data: [743, 656]}
	]
});
//плавное открытые блока
///////////////////////////////////////////////////////////////
function diplay_hide(block_id) {
  if ($(block_id).css('display') == 'none') {
    $(block_id).animate({ height: 'show' }, 500);
    document.getElementById('button_hide1').style.display = 'none';
    document.getElementById('button_hide2').style.display = 'none';

  }
  else {
    $(block_id).animate({ height: 'hide' }, 500);
    document.getElementById('button_hide1').style.display = 'block';
    document.getElementById('button_hide2').style.display = 'block';

  }
}
// 
