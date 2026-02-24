"""
Configuration management for Car Detailer Marketing Agent
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class MarketingChannels:
    """Marketing channel configurations"""
    social_media: List[str] = None
    email: bool = True
    local_seo: bool = True
    paid_ads: bool = True
    content_marketing: bool = True
    partnerships: bool = True
    referral: bool = True
    video: bool = True

    def __post_init__(self):
        if self.social_media is None:
            self.social_media = ["Instagram", "TikTok", "Facebook", "YouTube"]


@dataclass
class BusinessMetrics:
    """Key business metrics"""
    monthly_revenue: float
    average_customer_value: float
    repeat_customer_rate: float
    google_rating: float
    review_count: int
    current_customer_base: int
    monthly_inquiries: int
    conversion_rate: float


@dataclass
class MarketingConfig:
    """Main configuration for marketing strategies"""
    business_name: str
    business_type: str  # independent, franchise, dealership
    service_area: str
    monthly_budget: float
    channels: MarketingChannels
    metrics: Optional[BusinessMetrics] = None
    goals: List[str] = None
    unique_selling_points: List[str] = None
    target_demographics: List[str] = None

    def __post_init__(self):
        if self.goals is None:
            self.goals = ["Increase leads", "Build brand awareness"]
        if self.unique_selling_points is None:
            self.unique_selling_points = []
        if self.target_demographics is None:
            self.target_demographics = ["Vehicle owners aged 25-55"]


# Example configurations for different business types

INDEPENDENT_DETAILER_CONFIG = MarketingConfig(
    business_name="Independent Detailer",
    business_type="independent",
    service_area="Local City",
    monthly_budget=2000,
    channels=MarketingChannels(
        social_media=["Instagram", "TikTok", "Facebook"],
        email=True,
        local_seo=True,
        paid_ads=False,
        content_marketing=True,
        partnerships=True,
        referral=True,
        video=True
    ),
    goals=["Increase leads by 40%", "Build brand awareness", "Develop corporate clients"],
    unique_selling_points=["Premium ceramic coatings", "Eco-friendly products"],
    target_demographics=["Vehicle owners aged 30-55", "Small business owners"]
)

FRANCHISE_DETAILER_CONFIG = MarketingConfig(
    business_name="Franchise Detailer",
    business_type="franchise",
    service_area="Regional",
    monthly_budget=5000,
    channels=MarketingChannels(
        social_media=["Instagram", "TikTok", "Facebook", "YouTube"],
        email=True,
        local_seo=True,
        paid_ads=True,
        content_marketing=True,
        partnerships=True,
        referral=True,
        video=True
    ),
    goals=["Expand locations", "Increase customer base", "Build regional brand"],
    unique_selling_points=["Consistent quality across locations", "Warranty programs"],
    target_demographics=["Fleet owners", "Corporate clients", "Dealerships"]
)

DEALERSHIP_PARTNER_CONFIG = MarketingConfig(
    business_name="Dealership Partner",
    business_type="dealership",
    service_area="Local Area",
    monthly_budget=3000,
    channels=MarketingChannels(
        social_media=["Instagram", "Facebook"],
        email=True,
        local_seo=True,
        paid_ads=True,
        content_marketing=False,
        partnerships=True,
        referral=True,
        video=False
    ),
    goals=["Increase customer retention", "Upsell services", "Improve dealership ratings"],
    unique_selling_points=["Factory-approved products", "Warranty coverage"],
    target_demographics=["New car buyers", "Service customers", "Fleet services"]
)
