#import "MapPoint.h"

@implementation MapPoint

@synthesize coordinate = _coordinate;

- (void)setCoordinate:(CLLocationCoordinate2D)newCoordinate {
    [self willChangeValueForKey:@"coordinate"];
    [self willChangeValueForKey:@"title"];
    _coordinate = newCoordinate;
    [self didChangeValueForKey:@"coordinate"];
    [self didChangeValueForKey:@"title"];
}

- (id)initWithCoordinate:(CLLocationCoordinate2D)coordinate {
    
    self = [super init];
    
    if (self != nil)
    {
        _coordinate = coordinate;
    }
    
    return self;
}

-(NSString *)title {
    return [NSString stringWithFormat:@"%f,%f", _coordinate.latitude, _coordinate.longitude];
}

@end
