using CommunityToolkit.Mvvm.Input;
using CommunityToolkit.Mvvm.ComponentModel;

namespace ssaver.ViewModels;

public partial class MainWindowViewModel : ViewModelBase
{
    [ObservableProperty] private ViewModelBase current_page;
    [RelayCommand]
    public void clik()
    {
        current_page = new configsViewModel();
    }
    
}
