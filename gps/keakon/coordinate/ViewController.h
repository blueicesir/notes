#import <UIKit/UIKit.h>
#import <MapKit/MapKit.h>
#import <CoreLocation/CoreLocation.h>
#import "MapPoint.h"

@interface ViewController : UIViewController <CLLocationManagerDelegate> {
    MKMapView *mapView;
    CLLocationManager *locationManager;
    MapPoint* marsPoint;
    MapPoint* wgsPoint;
}

@end