namespace ssaver.ViewModels;
using CommunityToolkit.Mvvm.ComponentModel;

public partial class MainWindowViewModel  : ViewModelBase
{
    [ObservableProperty] private ViewModelBase current_page;
}