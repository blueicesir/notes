#import "ViewController.h"
#include "convert.h"

@implementation ViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
    
    mapView = [[MKMapView alloc] initWithFrame:CGRectMake(0, 0, 320, 480)];
//    mapView.mapType = MKMapTypeHybrid;
    mapView.showsUserLocation = YES;
    [self.view addSubview:mapView];
    
    
    if ([CLLocationManager locationServicesEnabled]) {
        locationManager = [[CLLocationManager alloc] init];
        locationManager.desiredAccuracy = kCLLocationAccuracyBestForNavigation;
        locationManager.delegate = self;
        [locationManager startUpdatingLocation];
    }
}

- (void)locationManager:(CLLocationManager *)manager
    didUpdateToLocation:(CLLocation *)newLocation
           fromLocation:(CLLocation *)oldLocation {
    CLLocationCoordinate2D coordinate = newLocation.coordinate;
    CLLocationCoordinate2D marsCoordinate = transform(coordinate);
    
//    NSLog(@"wgs: %f, %f", coordinate.latitude, coordinate.longitude);
//    NSLog(@"mars: %f, %f", marsCoordinate.latitude, marsCoordinate.longitude);
    
    if (wgsPoint) {
        [wgsPoint setCoordinate:coordinate];
    } else {
        wgsPoint = [[MapPoint alloc] initWithCoordinate:coordinate];
        [mapView addAnnotation:wgsPoint];
    }
    
    if (marsPoint) {
        [marsPoint setCoordinate:marsCoordinate];
        [mapView setCenterCoordinate:marsCoordinate animated:YES];
    } else {
        marsPoint = [[MapPoint alloc] initWithCoordinate:marsCoordinate];
        [mapView addAnnotation:marsPoint];
        mapView.region = MKCoordinateRegionMakeWithDistance(marsCoordinate, 100, 100);
    }
    
}

- (void)viewDidUnload {
    mapView = nil;
    wgsPoint = nil;
    marsPoint = nil;
    locationManager.delegate = nil;
    locationManager = nil;
}

@end
