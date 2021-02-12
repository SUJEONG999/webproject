
		function panTo(map_goo) {
    		// 이동할 위도 경도 위치를 생성합니다
    		if (map_goo == '강남구') {
    			var moveLatLon = new kakao.maps.LatLng(37.4959854, 127.0664091);
			}
			else if (map_goo == '강동구') {
    			var moveLatLon = new kakao.maps.LatLng(37.4959854, 127.0664091);
			}
			else if (map_goo == '강북구') {
    			var moveLatLon = new kakao.maps.LatLng(37.6469954, 127.0147158);
			}
			else if (map_goo == '강서구') {
    			var moveLatLon = new kakao.maps.LatLng(37.5657617, 126.8226561);
			}
			else if (map_goo == '관악구') {
    			var moveLatLon = new kakao.maps.LatLng(37.4653993, 126.9438071);
			}
			else if (map_goo == '광진구') {
    			var moveLatLon = new kakao.maps.LatLng(37.5481445, 127.0857528);
			}
			else if (map_goo == '구로구') {
    			var moveLatLon = new kakao.maps.LatLng(37.4954856, 126.858121);
			}
			else if (map_goo == '금천구') {
    			var moveLatLon = new kakao.maps.LatLng(37.4600969, 126.9001546);
			}
			else if (map_goo == '노원구') {
    			var moveLatLon = new kakao.maps.LatLng(37.655264, 127.0771201);
			}
			else if (map_goo == '도봉구') {
    			var moveLatLon = new kakao.maps.LatLng(37.6658609, 127.0317674);
			}
			else if (map_goo == '도봉구') {
    			var moveLatLon = new kakao.maps.LatLng(37.6658609, 127.0317674);
			}
			else if (map_goo == '동대문구') {
    			var moveLatLon = new kakao.maps.LatLng(37.5838012, 127.0507003);
			}
			else if (map_goo == '동작구') {
    			var moveLatLon = new kakao.maps.LatLng(37.4965037, 126.9443073);
			}
			else if (map_goo == '마포구') {
    			var moveLatLon = new kakao.maps.LatLng(37.5622906, 126.9087803);
			}
			else if (map_goo == '서대문구') {
    			var moveLatLon = new kakao.maps.LatLng(37.5820369, 126.9356665);
			}
			else if (map_goo == '서초구') {
    			var moveLatLon = new kakao.maps.LatLng(37.4769528, 127.0378103);
			}
			else if (map_goo == '성동구') {
    			var moveLatLon = new kakao.maps.LatLng(37.5506753, 127.0409622);
			}
			else if (map_goo == '성북구') {
    			var moveLatLon = new kakao.maps.LatLng(37.606991, 127.0232185);
			}
			else if (map_goo == '송파구') {
    			var moveLatLon = new kakao.maps.LatLng(37.5048534, 127.1144822);
			}
			else if (map_goo == '양천구') {
    			var moveLatLon = new kakao.maps.LatLng(37.5270616, 126.8561534);
			}
			else if (map_goo == '영등포구') {
    			var moveLatLon = new kakao.maps.LatLng(37.520641, 126.9139242);
			}
			else if (map_goo == '용산구') {
    			var moveLatLon = new kakao.maps.LatLng(37.5311008, 126.9810742);
			}
			else if (map_goo == '은평구') {
    			var moveLatLon = new kakao.maps.LatLng(37.6176125, 126.9227004);
			}
			else if (map_goo == '종로구') {
    			var moveLatLon = new kakao.maps.LatLng(37.5990998, 126.9861493);
			}
			else if (map_goo == '중구') {
    			var moveLatLon = new kakao.maps.LatLng(37.5579452, 126.9941904);
			}
			else {
    			var moveLatLon = new kakao.maps.LatLng(37.5953795, 127.0939669);
			}
  			// 지도 중심을 부드럽게 이동시킵니다
			// 만약 이동할 거리가 지도 화면보다 크면 부드러운 효과 없이 이동합니다
    		map.panTo(moveLatLon);
		}