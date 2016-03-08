
function initMap() {
  var latlong = {'lat': 58.1479823, 'lng': 7.920251800000001};
  var map = new google.maps.Map(document.getElementById('map'), {
    center: {"lng": -73.99384185740513, "lat": 40.76882096439725},
    zoom: 14,
    mapTypeId: google.maps.MapTypeId.TERRAIN
  });
  var jsonData = JSON.parse('[{"lng": -73.99384185740513, "lat": 40.76882096439725}, {"lng": -73.99384249763622, "lat": 40.7688212349026}, {"lng": -73.99393408667618, "lat": 40.768859932315955}, {"lng": -73.99469174294072, "lat": 40.769180046218416}, {"lng": -73.99469174294072, "lat": 40.769180046218416}, {"lng": -73.99469174294072, "lat": 40.769180046218416}, {"lng": -73.99469174294072, "lat": 40.769180046218416}, {"lng": -73.99469174294072, "lat": 40.769180046218416}, {"lng": -73.99469174294072, "lat": 40.769180046218416}, {"lng": -73.9948069, "lat": 40.7692287}, {"lng": -73.99481925645742, "lat": 40.76923502770579}, {"lng": -73.9948565, "lat": 40.7692541}, {"lng": -73.9948565, "lat": 40.7692541}, {"lng": -73.99479339999999, "lat": 40.7693486}, {"lng": -73.99479339999999, "lat": 40.7693486}, {"lng": -73.9945816, "lat": 40.7695284}, {"lng": -73.99443927784634, "lat": 40.76972149939175}, {"lng": -73.99443927784634, "lat": 40.76972149939175}, {"lng": -73.99443927784634, "lat": 40.76972149939175}, {"lng": -73.99436829999999, "lat": 40.76981779999999}, {"lng": -73.99434579715215, "lat": 40.7698543971638}, {"lng": -73.9943402, "lat": 40.7698635}, {"lng": -73.9943402, "lat": 40.7698635}, {"lng": -73.99432216331392, "lat": 40.769935059518446}, {"lng": -73.99431870000001, "lat": 40.7699488}, {"lng": -73.99431571702611, "lat": 40.76996369093465}, {"lng": -73.99429380000001, "lat": 40.77007309999999}, {"lng": -73.9942811, "lat": 40.7701469}, {"lng": -73.99427039999999, "lat": 40.770229199999996}, {"lng": -73.9942407760462, "lat": 40.770529345668926}, {"lng": -73.99423019999999, "lat": 40.77063649999999}, {"lng": -73.99423019999999, "lat": 40.77063649999999}, {"lng": -73.99330298673648, "lat": 40.77023869292039}, {"lng": -73.99265197790267, "lat": 40.76995937996862}, {"lng": -73.99218358232854, "lat": 40.769758412850486}, {"lng": -73.99190759999999, "lat": 40.769639999999995}, {"lng": -73.99190759999999, "lat": 40.769639999999995}, {"lng": -73.99089759529639, "lat": 40.769217983475905}, {"lng": -73.99048599999999, "lat": 40.769045999999996}, {"lng": -73.99048599999999, "lat": 40.769045999999996}, {"lng": -73.98966401076648, "lat": 40.768704262943935}, {"lng": -73.98904329999999, "lat": 40.7684462}, {"lng": -73.98904329999999, "lat": 40.7684462}, {"lng": -73.98865069630142, "lat": 40.76827902104457}, {"lng": -73.98742928400635, "lat": 40.76775890397835}, {"lng": -73.98674598196881, "lat": 40.76746792258647}, {"lng": -73.98674598196881, "lat": 40.76746792258647}, {"lng": -73.98673539105464, "lat": 40.767463412436996}, {"lng": -73.9862103, "lat": 40.7672398}, {"lng": -73.9862103, "lat": 40.7672398}, {"lng": -73.98584820894426, "lat": 40.767088342146494}, {"lng": -73.98476941405333, "lat": 40.766637085847925}, {"lng": -73.9847104, "lat": 40.76661239999999}, {"lng": -73.9847104, "lat": 40.76661239999999}, {"lng": -73.98462422082433, "lat": 40.76657634796672}, {"lng": -73.984538639948, "lat": 40.766540546122734}, {"lng": -73.98436744423074, "lat": 40.76646892792052}, {"lng": -73.98413608043958, "lat": 40.76637213829373}, {"lng": -73.9841039453206, "lat": 40.766358694704444}, {"lng": -73.9841039453206, "lat": 40.766358694704444}, {"lng": -73.9841039453206, "lat": 40.766358694704444}, {"lng": -73.9841039453206, "lat": 40.766358694704444}, {"lng": -73.9840389894385, "lat": 40.76633152064573}, {"lng": -73.98355085116745, "lat": 40.76612730788655}, {"lng": -73.9833663, "lat": 40.76605010000001}, {"lng": -73.9833663, "lat": 40.76605010000001}, {"lng": -73.9831764695585, "lat": 40.76631224144345}, {"lng": -73.9828696, "lat": 40.766736}, {"lng": -73.9828696, "lat": 40.766736}, {"lng": -73.98272939513781, "lat": 40.766940155006225}, {"lng": -73.9826497, "lat": 40.7670562}, {"lng": -73.9825469, "lat": 40.7671954}, {"lng": -73.9825469, "lat": 40.7671954}, {"lng": -73.98247961890684, "lat": 40.76728959355479}, {"lng": -73.9824689, "lat": 40.767304599999996}, {"lng": -73.98238959999999, "lat": 40.767411700000004}, {"lng": -73.98238959999999, "lat": 40.767411700000004}, {"lng": -73.98233189999999, "lat": 40.7674848}, {"lng": -73.982238, "lat": 40.767624999999995}, {"lng": -73.982238, "lat": 40.767624999999995}, {"lng": -73.9821667, "lat": 40.767676200000004}, {"lng": -73.9821103, "lat": 40.7677013}, {"lng": -73.9820835, "lat": 40.7677061}, {"lng": -73.9820458, "lat": 40.7677049}, {"lng": -73.9820458, "lat": 40.7677049}, {"lng": -73.9819589, "lat": 40.767694299999995}, {"lng": -73.98190939999999, "lat": 40.7676916}, {"lng": -73.9818545, "lat": 40.76769199999999}, {"lng": -73.9818545, "lat": 40.76769199999999}, {"lng": -73.9818102, "lat": 40.767694}, {"lng": -73.981778, "lat": 40.7676971}, {"lng": -73.98173079258376, "lat": 40.767706492058174}, {"lng": -73.98170664364025, "lat": 40.76771129655503}, {"lng": -73.98170534580365, "lat": 40.76771155476293}, {"lng": -73.9817016, "lat": 40.7677123}, {"lng": -73.9817016, "lat": 40.7677123}, {"lng": -73.9816681, "lat": 40.767735699999996}, {"lng": -73.9816305, "lat": 40.767759}, {"lng": -73.9815648, "lat": 40.7678118}, {"lng": -73.9815299, "lat": 40.7678423}, {"lng": -73.9814763, "lat": 40.767902199999995}, {"lng": -73.9814763, "lat": 40.767902199999995}, {"lng": -73.98144409999999, "lat": 40.7679459}, {"lng": -73.9813985, "lat": 40.7680119}, {"lng": -73.98137601065696, "lat": 40.76805228143336}, {"lng": -73.9813623, "lat": 40.7680769}, {"lng": -73.9813623, "lat": 40.7680769}, {"lng": -73.98136090000001, "lat": 40.7681034}, {"lng": -73.98136090000001, "lat": 40.7681034}, {"lng": -73.98137439999999, "lat": 40.768158199999995}, {"lng": -73.9813891, "lat": 40.768191699999996}, {"lng": -73.98141729999999, "lat": 40.7682456}, {"lng": -73.98141729999999, "lat": 40.7682456}, {"lng": -73.9814387, "lat": 40.7682791}, {"lng": -73.9814387, "lat": 40.7682791}, {"lng": -73.9814883, "lat": 40.76829939999999}, {"lng": -73.9816251, "lat": 40.768364399999996}, {"lng": -73.9816251, "lat": 40.768364399999996}, {"lng": -73.9819188, "lat": 40.768530999999996}, {"lng": -73.981951, "lat": 40.7685564}, {"lng": -73.981951, "lat": 40.7685564}, {"lng": -73.9819658, "lat": 40.7685726}, {"lng": -73.9819792, "lat": 40.7685939}, {"lng": -73.9819899, "lat": 40.768617299999995}, {"lng": -73.9819966, "lat": 40.7686437}, {"lng": -73.98199959982604, "lat": 40.76873887989776}, {"lng": -73.98200469999999, "lat": 40.768900699999996}, {"lng": -73.98200469999999, "lat": 40.768900699999996}, {"lng": -73.9819993, "lat": 40.769316100000005}, {"lng": -73.98200067247166, "lat": 40.769461856986545}, {"lng": -73.98200073838161, "lat": 40.76946885663069}, {"lng": -73.98200073838161, "lat": 40.76946885663069}, {"lng": -73.98200077604444, "lat": 40.76947285642736}, {"lng": -73.9820028, "lat": 40.7696878}, {"lng": -73.9820028, "lat": 40.7696878}, {"lng": -73.98201279999999, "lat": 40.7702403}, {"lng": -73.98201279999999, "lat": 40.7702403}, {"lng": -73.9820133274382, "lat": 40.77024474990036}, {"lng": -73.9820476, "lat": 40.770533900000004}, {"lng": -73.9820476, "lat": 40.770533900000004}, {"lng": -73.9820677, "lat": 40.7713586}, {"lng": -73.9820677, "lat": 40.7713586}, {"lng": -73.98207176393099, "lat": 40.77152595070191}, {"lng": -73.98208123058708, "lat": 40.771915779728275}, {"lng": -73.98208263731209, "lat": 40.7719737071034}, {"lng": -73.98208283929668, "lat": 40.77198202459639}, {"lng": -73.98208283929668, "lat": 40.77198202459639}, {"lng": -73.9820878, "lat": 40.7721863}, {"lng": -73.9820878, "lat": 40.7721863}, {"lng": -73.9820997316544, "lat": 40.7725959834592}, {"lng": -73.9821012, "lat": 40.7726464}, {"lng": -73.982112, "lat": 40.77288909999999}, {"lng": -73.982112, "lat": 40.77288909999999}, {"lng": -73.98211599999999, "lat": 40.7730059}, {"lng": -73.98211599999999, "lat": 40.7730059}, {"lng": -73.9821187, "lat": 40.7732091}, {"lng": -73.9821158, "lat": 40.7738432}, {"lng": -73.9821158, "lat": 40.7738432}, {"lng": -73.98210862302139, "lat": 40.7740595635295}, {"lng": -73.98209230799885, "lat": 40.774551405349044}, {"lng": -73.98209230799885, "lat": 40.774551405349044}, {"lng": -73.98209230799885, "lat": 40.774551405349044}, {"lng": -73.98209114772703, "lat": 40.77458638327672}, {"lng": -73.98208919999999, "lat": 40.7746451}, {"lng": -73.98208919999999, "lat": 40.7746451}, {"lng": -73.982069, "lat": 40.77544139999999}, {"lng": -73.982069, "lat": 40.77544139999999}, {"lng": -73.98206072668891, "lat": 40.775604602545634}, {"lng": -73.982027, "lat": 40.7762699}, {"lng": -73.982027, "lat": 40.7762699}, {"lng": -73.98202125405957, "lat": 40.77671814153693}, {"lng": -73.9820167, "lat": 40.7770734}, {"lng": -73.9820167, "lat": 40.7770734}, {"lng": -73.98199491955316, "lat": 40.777404996969956}, {"lng": -73.9819717, "lat": 40.777758500000004}, {"lng": -73.9819717, "lat": 40.777758500000004}, {"lng": -73.9819586, "lat": 40.7778523}, {"lng": -73.9819586, "lat": 40.7778523}, {"lng": -73.9819497, "lat": 40.777974199999996}, {"lng": -73.9819296, "lat": 40.7780768}, {"lng": -73.98192821940137, "lat": 40.778080658203834}, {"lng": -73.9818853, "lat": 40.7782006}, {"lng": -73.98184239999999, "lat": 40.7783052}, {"lng": -73.98184239999999, "lat": 40.7783052}, {"lng": -73.98175723762957, "lat": 40.77842617907554}, {"lng": -73.98175723762957, "lat": 40.77842617907554}, {"lng": -73.98175723762957, "lat": 40.77842617907554}, {"lng": -73.98172954729006, "lat": 40.77846551502198}, {"lng": -73.9816265, "lat": 40.77861190000001}, {"lng": -73.9816265, "lat": 40.77861190000001}, {"lng": -73.98126487864128, "lat": 40.77911523555518}, {"lng": -73.9811289, "lat": 40.779304499999995}, {"lng": -73.9811289, "lat": 40.779304499999995}, {"lng": -73.980673, "lat": 40.779925}, {"lng": -73.980673, "lat": 40.779925}, {"lng": -73.98065693322582, "lat": 40.77994740144149}, {"lng": -73.9802342, "lat": 40.7805368}, {"lng": -73.9802342, "lat": 40.7805368}, {"lng": -73.97979287363742, "lat": 40.78113425232223}, {"lng": -73.979748, "lat": 40.781195}, {"lng": -73.979748, "lat": 40.781195}, {"lng": -73.97928499999999, "lat": 40.781839000000005}, {"lng": -73.97928499999999, "lat": 40.781839000000005}, {"lng": -73.97896725950893, "lat": 40.782269532952746}, {"lng": -73.97882299999999, "lat": 40.782464999999995}, {"lng": -73.97882299999999, "lat": 40.782464999999995}, {"lng": -73.97846053515109, "lat": 40.78296238796514}, {"lng": -73.978326, "lat": 40.783147}, {"lng": -73.978326, "lat": 40.783147}, {"lng": -73.97809405059486, "lat": 40.783464944691275}, {"lng": -73.97782699999999, "lat": 40.783831}, {"lng": -73.97782699999999, "lat": 40.783831}, {"lng": -73.97740543176302, "lat": 40.78444960587536}, {"lng": -73.9773854, "lat": 40.784479}, {"lng": -73.9773854, "lat": 40.784479}, {"lng": -73.9769183, "lat": 40.7851075}, {"lng": -73.9769183, "lat": 40.7851075}, {"lng": -73.97661615176962, "lat": 40.78552788171938}, {"lng": -73.9764606, "lat": 40.7857443}, {"lng": -73.9764606, "lat": 40.7857443}, {"lng": -73.9759911, "lat": 40.78637559999999}, {"lng": -73.9759911, "lat": 40.78637559999999}, {"lng": -73.97579247144374, "lat": 40.78665998554687}, {"lng": -73.9755443, "lat": 40.78701529999999}, {"lng": -73.9755443, "lat": 40.78701529999999}, {"lng": -73.97518299324508, "lat": 40.78750518475322}, {"lng": -73.9750413, "lat": 40.7876973}, {"lng": -73.9750413, "lat": 40.7876973}, {"lng": -73.9745459, "lat": 40.78836659999999}, {"lng": -73.9745459, "lat": 40.78836659999999}, {"lng": -73.97447286029504, "lat": 40.78846767046196}, {"lng": -73.9740865, "lat": 40.7890023}, {"lng": -73.9740865, "lat": 40.7890023}, {"lng": -73.9737681074624, "lat": 40.78943117353408}, {"lng": -73.9736228, "lat": 40.789626899999995}, {"lng": -73.9736228, "lat": 40.789626899999995}, {"lng": -73.9731722, "lat": 40.7902516}, {"lng": -73.9731722, "lat": 40.7902516}, {"lng": -73.97295958193317, "lat": 40.7905593781871}, {"lng": -73.9727365, "lat": 40.7908823}, {"lng": -73.9727365, "lat": 40.7908823}, {"lng": -73.972267, "lat": 40.791511199999995}, {"lng": -73.972267, "lat": 40.791511199999995}, {"lng": -73.97211708444475, "lat": 40.791710896936614}, {"lng": -73.9717984, "lat": 40.7921354}, {"lng": -73.9717984, "lat": 40.7921354}, {"lng": -73.97133, "lat": 40.7927713}, {"lng": -73.97133, "lat": 40.7927713}, {"lng": -73.97129832767381, "lat": 40.79281214563189}, {"lng": -73.970858, "lat": 40.79337999999999}, {"lng": -73.970858, "lat": 40.79337999999999}, {"lng": -73.9706113149377, "lat": 40.793719050423}, {"lng": -73.9703639, "lat": 40.7940591}, {"lng": -73.9703639, "lat": 40.7940591}, {"lng": -73.96987, "lat": 40.79473600000001}, {"lng": -73.96987, "lat": 40.79473600000001}, {"lng": -73.96985058941904, "lat": 40.79476266316273}, {"lng": -73.969415, "lat": 40.795361}, {"lng": -73.969415, "lat": 40.795361}, {"lng": -73.96936850960428, "lat": 40.79542450711009}, {"lng": -73.96896124007792, "lat": 40.795980842062164}, {"lng": -73.96895599999999, "lat": 40.795988}, {"lng": -73.96895599999999, "lat": 40.795988}, {"lng": -73.9684943, "lat": 40.7966173}, {"lng": -73.9684943, "lat": 40.7966173}, {"lng": -73.9682981752891, "lat": 40.796889245823834}, {"lng": -73.96803799999999, "lat": 40.797250000000005}, {"lng": -73.96803799999999, "lat": 40.797250000000005}, {"lng": -73.96758155361782, "lat": 40.797861224190775}, {"lng": -73.967575, "lat": 40.797869999999996}, {"lng": -73.967575, "lat": 40.797869999999996}, {"lng": -73.96712, "lat": 40.798503}, {"lng": -73.96712, "lat": 40.798503}, {"lng": -73.96674175658654, "lat": 40.79901614702537}, {"lng": -73.9666512, "lat": 40.799139}, {"lng": -73.9666512, "lat": 40.799139}, {"lng": -73.96593122283704, "lat": 40.79882152452661}, {"lng": -73.96584930000002, "lat": 40.7987854}, {"lng": -73.96584930000002, "lat": 40.7987854}, {"lng": -73.96498738895635, "lat": 40.79841196815307}, {"lng": -73.96406955644328, "lat": 40.79801429608251}]');
  var path = new google.maps.Polyline({
    path: jsonData,
    geodesic: true,
    strokeColor: '#FF0000',
    strokeOpacity: 1.0,
    strokeWieght: 2
  });
  path.setMap(map);
}
