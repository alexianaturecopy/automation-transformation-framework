"""
Automation Transformation Framework - Interactive Dashboard
Demonstrates before/after transformation for multi-national manufacturing enterprise
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Automation Transformation Framework",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #2c3e50;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
        margin-bottom: 1rem;
    }
    .improvement-positive {
        color: #27ae60;
        font-weight: bold;
    }
    .improvement-negative {
        color: #e74c3c;
        font-weight: bold;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    """Load transformation metrics data"""
    data_path = Path(__file__).parent / "data"
    
    current_state = pd.read_csv(data_path / "current_state_metrics.csv")
    target_state = pd.read_csv(data_path / "target_state_metrics.csv")
    roi_projections = pd.read_csv(data_path / "roi_projections.csv")
    process_inventory = pd.read_csv(data_path / "process_inventory.csv")
    
    return current_state, target_state, roi_projections, process_inventory

# Initialize session state
if 'show_comparison' not in st.session_state:
    st.session_state.show_comparison = False

# Load data
current_state, target_state, roi_projections, process_inventory = load_data()

# Sidebar navigation
st.sidebar.markdown("## 🏭 Navigation")
page = st.sidebar.radio(
    "Select View:",
    ["Executive Summary", "Current State Analysis", "Target State Vision", 
     "Transformation Journey", "ROI Calculator", "Risk Assessment"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Quick Stats")
st.sidebar.metric("Total Investment", "$3.8M", "Over 24 months")
st.sidebar.metric("Annual Savings", "$9.2M", "Recurring benefit")
st.sidebar.metric("Payback Period", "14 months", "-62% faster")
st.sidebar.metric("3-Year NPV", "$18.4M", "187% IRR")

st.sidebar.markdown("---")
st.sidebar.markdown("**Company Profile:**")
st.sidebar.markdown("🏢 Multi-national Manufacturing")
st.sidebar.markdown("💰 $850M Revenue")
st.sidebar.markdown("👥 3,500 Employees")
st.sidebar.markdown("🌍 15 Countries")

# =======================
# PAGE 1: EXECUTIVE SUMMARY
# =======================
if page == "Executive Summary":
    st.markdown('<div class="main-header">🏭 Automation Transformation Framework</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: center; font-size: 1.2rem; color: #7f8c8d; margin-bottom: 2rem;">Strategic Digital Transformation for Multi-National Manufacturing</div>', unsafe_allow_html=True)
    
    # Key metrics comparison
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Month-End Close",
            "5 days",
            "-5 days (50%)",
            help="Current: 10 days → Target: 5 days"
        )
    
    with col2:
        st.metric(
            "Order-to-Cash",
            "5 days",
            "-7 days (58%)",
            help="Current: 12 days → Target: 5 days"
        )
    
    with col3:
        st.metric(
            "Manual Hours",
            "12K/year",
            "-33K (73%)",
            help="Current: 45K hours → Target: 12K hours"
        )
    
    with col4:
        st.metric(
            "Error Rate",
            "0.8%",
            "-3.4% (81%)",
            help="Current: 4.2% → Target: 0.8%"
        )
    
    st.markdown("---")
    
    # Ten automation domains
    st.markdown('<div class="sub-header">📊 Ten Automation Domains</div>', unsafe_allow_html=True)
    
    domains_data = {
        'Domain': [
            '1. Order-to-Cash',
            '2. Inventory Management',
            '3. Intercompany Transactions',
            '4. R&D Capitalization',
            '5. Accounting & Tax',
            '6. Procure-to-Pay',
            '7. Production Planning',
            '8. Quality Management',
            '9. Consolidation & Reporting',
            '10. Treasury & Cash Mgmt'
        ],
        'Current Pain Point': [
            '15 manual handoffs, 12-day cycle',
            '8% stockouts, 60-day turns',
            '8-day close extension',
            'Manual quarterly reviews',
            '10-day close, manual calcs',
            '3-way matching errors, delays',
            'Manual MRP, capacity issues',
            'Paper-based inspections',
            'Manual eliminations, 10-day close',
            'Manual cash forecasting, FX risk'
        ],
        'Target State': [
            '3 touchpoints, 5-day cycle',
            '2% stockouts, 30-day turns',
            '3-day automated close',
            'Real-time tracking',
            '5-day close, 80% automated',
            'Automated matching, 5-day cycle',
            'Automated MRP, real-time capacity',
            'Mobile QC, automated CAPA',
            'Automated IC, 5-day close',
            'AI cash forecasting, auto-hedging'
        ],
        'Annual Benefit': [
            '$2.3M',
            '$4.5M',
            '$800K',
            '$600K',
            '$1.2M',
            '$1.8M',
            '$1.5M',
            '$900K',
            '$1.1M',
            '$700K'
        ]
    }
    
    domains_df = pd.DataFrame(domains_data)
    st.dataframe(domains_df, use_container_width=True, hide_index=True)
    
    # Financial summary
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="sub-header">💰 Financial Impact</div>', unsafe_allow_html=True)
        
        financial_data = {
            'Metric': ['Total Investment', 'Annual Benefit', 'NPV (3 years)', 'IRR', 'Payback Period'],
            'Value': ['$3.8M', '$9.2M', '$18.4M', '187%', '14 months']
        }
        st.table(pd.DataFrame(financial_data))
    
    with col2:
        st.markdown('<div class="sub-header">📈 Benefit Breakdown</div>', unsafe_allow_html=True)
        
        # Benefit pie chart
        benefit_data = {
            'Category': ['Inventory Optimization', 'Order-to-Cash', 'Procure-to-Pay', 
                        'Production Planning', 'Consolidation', 'Tax & Accounting',
                        'Intercompany', 'Quality Management', 'Treasury', 'R&D Cap'],
            'Amount': [4.5, 2.3, 1.8, 1.5, 1.1, 1.2, 0.8, 0.9, 0.7, 0.6]
        }
        
        fig = px.pie(
            pd.DataFrame(benefit_data),
            values='Amount',
            names='Category',
            title='$9.2M Annual Benefit Distribution',
            hole=0.4
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)

# =======================
# PAGE 2: CURRENT STATE ANALYSIS
# =======================
elif page == "Current State Analysis":
    st.markdown('<div class="main-header">🔴 Current State: Pain Points & Challenges</div>', unsafe_allow_html=True)
    
    # Overall metrics
    st.markdown('<div class="sub-header">📊 Current Operational Metrics</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Close Cycle", "10 days", help="Month-end close duration")
    with col2:
        st.metric("OTC Cycle", "12 days", help="Order-to-Cash cycle time")
    with col3:
        st.metric("Stockout Rate", "8%", help="Inventory availability issues")
    with col4:
        st.metric("Manual Hours", "45K/year", help="Annual manual process hours")
    with col5:
        st.metric("Error Rate", "4.2%", help="Process error percentage")
    
    # Process metrics comparison
    st.markdown("---")
    st.markdown('<div class="sub-header">⚠️ Process Performance (Current State)</div>', unsafe_allow_html=True)
    
    # Bar chart of cycle times
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Current State',
        x=current_state['process_name'],
        y=current_state['cycle_time_days'],
        marker_color='#e74c3c',
        text=current_state['cycle_time_days'],
        textposition='auto',
    ))
    
    fig.update_layout(
        title='Process Cycle Times (Days) - Current State',
        xaxis_title='Process',
        yaxis_title='Days',
        height=400,
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Cost analysis
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="sub-header">💸 Inefficiency Costs</div>', unsafe_allow_html=True)
        
        # Cost breakdown bar chart
        fig = px.bar(
            current_state,
            x='annual_cost_impact',
            y='process_name',
            orientation='h',
            title='Annual Cost of Inefficiency by Process',
            labels={'annual_cost_impact': 'Annual Cost ($M)', 'process_name': 'Process'},
            color='annual_cost_impact',
            color_continuous_scale='Reds'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown('<div class="sub-header">⏱️ Manual Labor Distribution</div>', unsafe_allow_html=True)
        
        # FTE allocation
        fig = px.pie(
            current_state,
            values='fte_equivalent',
            names='process_name',
            title='FTE Allocation Across Processes',
            hole=0.4
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Detailed metrics table
    st.markdown("---")
    st.markdown('<div class="sub-header">📋 Detailed Process Metrics</div>', unsafe_allow_html=True)
    
    display_df = current_state[[
        'process_name', 'cycle_time_days', 'manual_hours_per_year', 
        'error_rate_pct', 'annual_cost_impact', 'fte_equivalent'
    ]].copy()
    
    display_df.columns = ['Process', 'Cycle Time (days)', 'Manual Hours/Year', 
                          'Error Rate %', 'Annual Cost ($M)', 'FTE']
    
    st.dataframe(display_df, use_container_width=True, hide_index=True)
    
    # Key problems
    st.markdown("---")
    st.markdown('<div class="sub-header">🚨 Critical Issues</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.error("**Process Delays**")
        st.markdown("""
        - 10-day month-end close
        - 12-day Order-to-Cash cycle
        - 8-day IC close extension
        - Slow decision-making
        """)
    
    with col2:
        st.error("**High Manual Effort**")
        st.markdown("""
        - 45,000 manual hours/year
        - 15 handoffs in OTC
        - Manual IC reconciliation
        - Spreadsheet-based processes
        """)
    
    with col3:
        st.error("**Quality Issues**")
        st.markdown("""
        - 4.2% average error rate
        - 8% inventory stockouts
        - Compliance risks
        - Audit inefficiencies
        """)

# =======================
# PAGE 3: TARGET STATE VISION
# =======================
elif page == "Target State Vision":
    st.markdown('<div class="main-header">✅ Target State: Transformed Operations</div>', unsafe_allow_html=True)
    
    # Overall metrics
    st.markdown('<div class="sub-header">📊 Target Operational Metrics</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Close Cycle", "5 days", "-5 days", delta_color="normal")
    with col2:
        st.metric("OTC Cycle", "5 days", "-7 days", delta_color="normal")
    with col3:
        st.metric("Stockout Rate", "2%", "-6%", delta_color="normal")
    with col4:
        st.metric("Manual Hours", "12K/year", "-33K", delta_color="normal")
    with col5:
        st.metric("Error Rate", "0.8%", "-3.4%", delta_color="normal")
    
    # Before/After comparison
    st.markdown("---")
    st.markdown('<div class="sub-header">📈 Before vs After Transformation</div>', unsafe_allow_html=True)
    
    # Cycle time comparison
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Current State',
        x=current_state['process_name'],
        y=current_state['cycle_time_days'],
        marker_color='#e74c3c',
        text=current_state['cycle_time_days'].astype(str) + 'd',
        textposition='auto',
    ))
    
    fig.add_trace(go.Bar(
        name='Target State',
        x=target_state['process_name'],
        y=target_state['cycle_time_days'],
        marker_color='#27ae60',
        text=target_state['cycle_time_days'].astype(str) + 'd',
        textposition='auto',
    ))
    
    fig.update_layout(
        title='Cycle Time Reduction: Current vs Target',
        xaxis_title='Process',
        yaxis_title='Days',
        barmode='group',
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Improvement metrics
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="sub-header">⚡ Efficiency Gains</div>', unsafe_allow_html=True)
        
        # Calculate improvements
        improvements = pd.DataFrame({
            'Process': target_state['process_name'],
            'Cycle Time Reduction %': ((current_state['cycle_time_days'] - target_state['cycle_time_days']) / 
                                       current_state['cycle_time_days'] * 100).round(1),
            'Manual Hours Reduction %': ((current_state['manual_hours_per_year'] - target_state['manual_hours_per_year']) / 
                                         current_state['manual_hours_per_year'] * 100).round(1)
        })
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            name='Cycle Time Reduction',
            x=improvements['Process'],
            y=improvements['Cycle Time Reduction %'],
            marker_color='#3498db'
        ))
        
        fig.add_trace(go.Bar(
            name='Manual Hours Reduction',
            x=improvements['Process'],
            y=improvements['Manual Hours Reduction %'],
            marker_color='#9b59b6'
        ))
        
        fig.update_layout(
            title='Improvement Percentage by Process',
            xaxis_title='Process',
            yaxis_title='Reduction %',
            barmode='group',
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown('<div class="sub-header">💰 Cost Savings</div>', unsafe_allow_html=True)
        
        # Savings waterfall
        categories = ['Current Cost', 'Labor Savings', 'Error Reduction', 
                     'Process Efficiency', 'Working Capital', 'Target Cost']
        values = [12.8, -3.8, -2.5, -2.0, -4.5, 0]
        
        fig = go.Figure(go.Waterfall(
            name="Cost",
            orientation="v",
            measure=["relative", "relative", "relative", "relative", "relative", "total"],
            x=categories,
            textposition="outside",
            text=["+$12.8M", "-$3.8M", "-$2.5M", "-$2.0M", "-$4.5M", "$0M"],
            y=values,
            connector={"line": {"color": "rgb(63, 63, 63)"}},
        ))
        
        fig.update_layout(
            title="Annual Cost Reduction Waterfall ($M)",
            showlegend=False,
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Key capabilities
    st.markdown("---")
    st.markdown('<div class="sub-header">🎯 Key Capabilities Enabled</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.success("**Real-Time Visibility**")
        st.markdown("""
        - Live dashboard for all processes
        - Automated alerts for exceptions
        - Mobile access for approvals
        - Executive KPI tracking
        """)
    
    with col2:
        st.success("**Automated Workflows**")
        st.markdown("""
        - API-based integrations
        - Rule-based approvals
        - Automated reconciliations
        - Exception-only processing
        """)
    
    with col3:
        st.success("**Predictive Analytics**")
        st.markdown("""
        - AI-powered forecasting
        - Demand prediction
        - Cash flow forecasting
        - Risk identification
        """)

# =======================
# PAGE 4: TRANSFORMATION JOURNEY
# =======================
elif page == "Transformation Journey":
    st.markdown('<div class="main-header">🚀 24-Month Transformation Journey</div>', unsafe_allow_html=True)
    
    # Phase overview
    st.markdown('<div class="sub-header">📅 Four-Phase Implementation</div>', unsafe_allow_html=True)
    
    phases = [
        {
            'phase': 'Phase 1',
            'name': 'Foundation & Quick Wins',
            'duration': 'Months 1-3',
            'investment': '$450K',
            'benefit': '$500K',
            'risk': 'Low',
            'key_activities': [
                'Process documentation',
                'Quick win automation (invoicing, approvals)',
                'Infrastructure setup',
                'Team training'
            ]
        },
        {
            'phase': 'Phase 2',
            'name': 'Core Business Automation',
            'duration': 'Months 4-9',
            'investment': '$1.5M',
            'benefit': '$3.5M cumulative',
            'risk': 'Medium',
            'key_activities': [
                'Order-to-Cash automation',
                'Inventory optimization',
                'IC transaction automation',
                'Procure-to-Pay automation'
            ]
        },
        {
            'phase': 'Phase 3',
            'name': 'Advanced Capabilities',
            'duration': 'Months 10-18',
            'investment': '$1.2M',
            'benefit': '$5.0M cumulative',
            'risk': 'Controlled',
            'key_activities': [
                'Predictive analytics',
                'Production planning automation',
                'Quality management digitization',
                'Treasury automation'
            ]
        },
        {
            'phase': 'Phase 4',
            'name': 'Scale & Optimize',
            'duration': 'Months 19-24',
            'investment': '$650K',
            'benefit': '$9.2M full run-rate',
            'risk': 'Proven',
            'key_activities': [
                'Global rollout (15 countries)',
                'Process optimization',
                'Advanced analytics',
                'Center of Excellence'
            ]
        }
    ]
    
    # Create phase cards
    for i, phase in enumerate(phases):
        with st.expander(f"**{phase['phase']}: {phase['name']}** ({phase['duration']})", expanded=(i==0)):
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Investment", phase['investment'])
            with col2:
                st.metric("Benefit", phase['benefit'])
            with col3:
                st.metric("Risk Level", phase['risk'])
            with col4:
                roi_val = float(phase['benefit'].replace('$', '').replace('M', '').split()[0])
                inv_val = float(phase['investment'].replace('$', '').replace('K', '').replace('M', '')) / (1000 if 'K' in phase['investment'] else 1)
                st.metric("ROI Multiple", f"{(roi_val/inv_val):.1f}x")
            
            st.markdown("**Key Activities:**")
            for activity in phase['key_activities']:
                st.markdown(f"- {activity}")
    
    # Timeline visualization
    st.markdown("---")
    st.markdown('<div class="sub-header">📊 Benefit Realization Timeline</div>', unsafe_allow_html=True)
    
    # Cumulative benefit chart
    months = list(range(0, 25))
    cumulative_benefit = [0, 0, 0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 
                         4.0, 4.2, 4.4, 4.6, 4.8, 5.0, 5.5, 6.0, 6.5,
                         7.0, 7.5, 8.0, 8.5, 9.0, 9.2]
    cumulative_investment = [0, 0.15, 0.30, 0.45, 0.95, 1.45, 1.95, 2.45, 2.95, 3.15,
                            3.35, 3.55, 3.75, 3.95, 4.15, 4.35, 4.55, 4.75, 4.95,
                            5.15, 5.35, 5.55, 5.75, 5.95, 6.00]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=months,
        y=cumulative_benefit,
        name='Cumulative Benefit',
        line=dict(color='#27ae60', width=3),
        fill='tozeroy'
    ))
    
    fig.add_trace(go.Scatter(
        x=months,
        y=cumulative_investment,
        name='Cumulative Investment',
        line=dict(color='#e74c3c', width=3, dash='dash')
    ))
    
    # Add payback marker
    fig.add_vline(x=14, line_dash="dot", line_color="gray", 
                  annotation_text="Payback: Month 14", annotation_position="top")
    
    fig.update_layout(
        title='Cumulative Benefit vs Investment Over 24 Months',
        xaxis_title='Month',
        yaxis_title='Amount ($M)',
        height=400,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # ROI projections table
    st.markdown("---")
    st.markdown('<div class="sub-header">💰 Financial Projections by Phase</div>', unsafe_allow_html=True)
    
    display_roi = roi_projections.copy()
    display_roi.columns = ['Phase', 'Investment ($M)', 'Annual Benefit ($M)', 
                          'Cumulative Benefit ($M)', 'Payback (Months)']
    st.dataframe(display_roi, use_container_width=True, hide_index=True)

# =======================
# PAGE 5: ROI CALCULATOR
# =======================
elif page == "ROI Calculator":
    st.markdown('<div class="main-header">💰 Interactive ROI Calculator</div>', unsafe_allow_html=True)
    
    st.markdown("""
    Adjust the assumptions below to see how different scenarios impact the business case.
    Use this tool to model conservative, base, and optimistic cases.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="sub-header">📊 Assumptions</div>', unsafe_allow_html=True)
        
        # Investment sliders
        st.markdown("**Investment Parameters:**")
        phase1_investment = st.slider("Phase 1 Investment ($K)", 300, 600, 450, 50)
        phase2_investment = st.slider("Phase 2 Investment ($M)", 1.0, 2.0, 1.5, 0.1)
        phase3_investment = st.slider("Phase 3 Investment ($M)", 0.8, 1.6, 1.2, 0.1)
        phase4_investment = st.slider("Phase 4 Investment ($K)", 400, 900, 650, 50)
        
        total_investment = (phase1_investment / 1000) + phase2_investment + phase3_investment + (phase4_investment / 1000)
        
        st.markdown("**Benefit Parameters:**")
        benefit_realization = st.slider("Benefit Realization %", 50, 120, 100, 5)
        timeline_months = st.slider("Implementation Timeline (months)", 18, 36, 24, 3)
        discount_rate = st.slider("Discount Rate %", 5, 15, 10, 1)
        
    with col2:
        st.markdown('<div class="sub-header">📈 Calculated Results</div>', unsafe_allow_html=True)
        
        # Calculate results
        annual_benefit = 9.2 * (benefit_realization / 100)
        year1_benefit = annual_benefit * 0.4  # Partial year
        year2_benefit = annual_benefit * 0.8  # Ramping up
        year3_benefit = annual_benefit  # Full run-rate
        
        # NPV calculation
        npv = -total_investment
        for year, benefit in enumerate([year1_benefit, year2_benefit, year3_benefit], 1):
            npv += benefit / ((1 + discount_rate/100) ** year)
        
        # Payback
        cumulative = 0
        payback_months = 0
        monthly_benefit = annual_benefit / 12
        for month in range(1, 61):  # Max 5 years
            cumulative += monthly_benefit - (total_investment / timeline_months if month <= timeline_months else 0)
            if cumulative >= 0:
                payback_months = month
                break
        
        # Display metrics
        st.metric("Total Investment", f"${total_investment:.1f}M")
        st.metric("Annual Benefit (Full Run-Rate)", f"${annual_benefit:.1f}M")
        st.metric("NPV (3 years)", f"${npv:.1f}M", 
                 delta=f"{((npv/total_investment)*100):.0f}% return")
        st.metric("Payback Period", f"{payback_months} months")
        
        if npv > 0:
            irr = ((npv / total_investment + 1) ** (1/3) - 1) * 100
            st.metric("Estimated IRR", f"{irr:.0f}%")
    
    # Scenario comparison
    st.markdown("---")
    st.markdown('<div class="sub-header">📊 Scenario Analysis</div>', unsafe_allow_html=True)
    
    scenarios = {
        'Scenario': ['Pessimistic (60%)', 'Base Case (100%)', 'Optimistic (120%)'],
        'Annual Benefit': ['$5.5M', '$9.2M', '$11.0M'],
        'NPV (3yr)': ['$8.2M', '$18.4M', '$24.8M'],
        'Payback': ['22 months', '14 months', '11 months'],
        'IRR': ['89%', '187%', '245%']
    }
    
    scenarios_df = pd.DataFrame(scenarios)
    st.dataframe(scenarios_df, use_container_width=True, hide_index=True)
    
    # Sensitivity analysis
    st.markdown("---")
    st.markdown('<div class="sub-header">🎯 Sensitivity Analysis</div>', unsafe_allow_html=True)
    
    st.markdown("""
    **Key Sensitivities:**
    - **Benefit Realization:** Even at 60% realization, NPV remains strongly positive ($8.2M)
    - **Timeline:** Extending to 36 months delays payback but maintains positive ROI
    - **Investment Overrun:** 20% cost overrun still yields NPV > $15M
    - **Discount Rate:** Break-even at ~35% discount rate (far above typical hurdle rates)
    """)
    
    # Benefit breakdown
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Benefit Sources:**")
        benefit_sources = {
            'Category': ['Labor Reduction', 'Error Elimination', 'Working Capital', 
                        'Process Efficiency', 'Revenue Protection'],
            'Amount': [3.8, 2.5, 4.5, 2.0, 1.9]
        }
        fig = px.pie(pd.DataFrame(benefit_sources), values='Amount', names='Category',
                    title='Benefit Composition ($M)')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("**Investment Allocation:**")
        investment_sources = {
            'Category': ['Software & Licenses', 'Implementation Services', 
                        'Training & Change Mgmt', 'Infrastructure', 'Contingency'],
            'Amount': [1.2, 1.5, 0.6, 0.3, 0.2]
        }
        fig = px.pie(pd.DataFrame(investment_sources), values='Amount', names='Category',
                    title='Investment Breakdown ($M)')
        st.plotly_chart(fig, use_container_width=True)

# =======================
# PAGE 6: RISK ASSESSMENT
# =======================
elif page == "Risk Assessment":
    st.markdown('<div class="main-header">⚠️ Risk Assessment & Mitigation</div>', unsafe_allow_html=True)
    
    # Risk matrix
    st.markdown('<div class="sub-header">🎯 Risk Matrix</div>', unsafe_allow_html=True)
    
    risks = pd.DataFrame({
        'Risk': [
            'System Integration Failures',
            'User Adoption Resistance',
            'Data Quality Issues',
            'Cost Overruns',
            'Timeline Delays',
            'Key Person Dependency',
            'Security & Compliance',
            'Vendor Dependency',
            'Business Process Changes',
            'ROI Not Achieved'
        ],
        'Probability': ['Medium', 'High', 'Medium', 'Medium', 'Medium', 
                       'Medium', 'Low', 'Low', 'Low', 'Low'],
        'Impact': ['High', 'High', 'Medium', 'Medium', 'Medium',
                  'Medium', 'High', 'Medium', 'Medium', 'High'],
        'Score': [6, 8, 4, 4, 4, 4, 3, 2, 2, 3],
        'Mitigation': [
            'Parallel runs, extensive UAT, rollback procedures',
            'Change management program, quick wins, power users',
            'Data quality assessment, automated validation',
            'Detailed budgeting, 15% contingency, gate reviews',
            'Realistic timeline, weekly tracking, buffer time',
            'Cross-training, documentation, vendor backup',
            'Security review, compliance maintained, audit trail',
            'Open-source preference, multi-year contracts',
            'Flexible architecture, configurable rules',
            'Conservative assumptions, monthly benefit tracking'
        ]
    })
    
    # Create risk score mapping
    prob_map = {'Low': 1, 'Medium': 2, 'High': 3}
    impact_map = {'Low': 1, 'Medium': 2, 'High': 3}
    
    risks['Prob_Numeric'] = risks['Probability'].map(prob_map)
    risks['Impact_Numeric'] = risks['Impact'].map(impact_map)
    
    # Risk matrix scatter plot
    fig = px.scatter(
        risks,
        x='Prob_Numeric',
        y='Impact_Numeric',
        size='Score',
        color='Score',
        hover_data=['Risk'],
        labels={'Prob_Numeric': 'Probability', 'Impact_Numeric': 'Impact'},
        title='Risk Matrix: Probability vs Impact',
        color_continuous_scale='RdYlGn_r'
    )
    
    fig.update_xaxes(tickvals=[1, 2, 3], ticktext=['Low', 'Medium', 'High'])
    fig.update_yaxes(tickvals=[1, 2, 3], ticktext=['Low', 'Medium', 'High'])
    
    # Add quadrant shading
    fig.add_shape(type="rect", x0=0.5, y0=0.5, x1=2.5, y1=2.5,
                  fillcolor="green", opacity=0.1, line_width=0)
    fig.add_shape(type="rect", x0=2.5, y0=2.5, x1=3.5, y1=3.5,
                  fillcolor="red", opacity=0.1, line_width=0)
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Risk details
    st.markdown("---")
    st.markdown('<div class="sub-header">📋 Risk Register</div>', unsafe_allow_html=True)
    
    # Display top risks
    top_risks = risks.nlargest(5, 'Score')[['Risk', 'Probability', 'Impact', 'Score', 'Mitigation']]
    
    for _, risk in top_risks.iterrows():
        with st.expander(f"**{risk['Risk']}** (Score: {risk['Score']})"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Probability", risk['Probability'])
            with col2:
                st.metric("Impact", risk['Impact'])
            with col3:
                st.metric("Risk Score", risk['Score'])
            
            st.markdown("**Mitigation Strategy:**")
            st.write(risk['Mitigation'])
    
    # Risk by phase
    st.markdown("---")
    st.markdown('<div class="sub-header">📅 Risk Profile by Phase</div>', unsafe_allow_html=True)
    
    phase_risk = pd.DataFrame({
        'Phase': ['Phase 1', 'Phase 2', 'Phase 3', 'Phase 4'],
        'Overall Risk': ['Low', 'Medium', 'Controlled', 'Proven'],
        'Primary Concerns': [
            'Quick win delivery, stakeholder alignment',
            'Integration complexity, user adoption',
            'Advanced features, predictive model accuracy',
            'Global rollout coordination, sustainability'
        ],
        'Risk Score': [2, 5, 4, 2]
    })
    
    fig = px.bar(
        phase_risk,
        x='Phase',
        y='Risk Score',
        color='Overall Risk',
        title='Risk Score by Implementation Phase',
        color_discrete_map={'Low': '#27ae60', 'Medium': '#f39c12', 
                           'Controlled': '#3498db', 'Proven': '#27ae60'}
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Mitigation strategies
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.success("**Technical Mitigation**")
        st.markdown("""
        - Parallel processing during transition
        - Comprehensive testing protocols
        - Automated rollback procedures
        - Vendor support agreements
        - Regular security audits
        """)
    
    with col2:
        st.success("**Organizational Mitigation**")
        st.markdown("""
        - Executive sponsorship
        - Change management program
        - Power user network
        - Training and support
        - Communication plan
        """)
    
    with col3:
        st.success("**Financial Mitigation**")
        st.markdown("""
        - 15% contingency budget
        - Gate review process
        - Benefit tracking from Day 1
        - Conservative assumptions
        - Scenario analysis
        """)

# Footer
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Framework Version:** 1.0")
with col2:
    st.markdown("**Last Updated:** December 2024")
with col3:
    st.markdown("**Status:** ✅ Complete")
